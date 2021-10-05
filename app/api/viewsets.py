from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from . import models
from . import serializers


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     return Response('Jopa')
