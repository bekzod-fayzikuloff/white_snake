"""
There we make all us `ViewSets` for using
in us api router
"""
from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from . import models
from . import serializers
from . import services


class CompanyViewSet(viewsets.ModelViewSet):
    """
    CompanyViewSet extends rest_framework.viewsets.ModelViewSet
    and make all need functional(CRUD)
    """

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PersonViewSet(viewsets.ModelViewSet):
    """
    CompanyViewSet extends rest_framework.viewsets.ModelViewSet
    and make all need functional(CRUD)
    """

    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Rewrite retrieve() method with some changing on serialized data on `detail`
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        obj = get_object_or_404(models.Person, pk=kwargs.get("pk"))
        serializer_obj = serializers.PersonSerializer(obj).data.copy()
        language_pk_list = serializer_obj["language"]
        language_data = []

        for language_pk in language_pk_list:
            language_data.append(services.get_person_language_data(id_=language_pk))

        serializer_obj["language_detail"] = language_data
        return Response(serializer_obj)


class LanguageViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    """
    class LanguageViewSet multiple extends with CRUD mixins,
    and rest_framework.viewsets.GenericViewSet and realize CRUD functionality
    on one simple class with overwrite list(), retrieve(), create(), update() methods
    """

    serializer_class = serializers.LanguageSerializer
    queryset = models.Language.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Getting all model records and serialize this records data
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer_data = serializers.LanguageSerializer(
            self.get_queryset(), many=True
        ).data
        return Response(serializer_data)

    def create(self, request, *args, **kwargs):
        """
        Add new record on model and retrieve this record after serializing
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        """
        Change record field value
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Getting model instance and serialize this instance
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        language_instance = get_object_or_404(models.Language, pk=kwargs.get("pk"))
        return Response(serializers.LanguageSerializer(language_instance).data)
