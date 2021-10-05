from django.http import Http404
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from . import services
from .serializers import CompanySerializer, OfficeSerializer
from .models import Company, Office, Person


class OfficeView(generics.UpdateAPIView,
                 generics.DestroyAPIView,
                 APIView
                 ):
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            queryset = self.get_queryset()
            serializer = OfficeSerializer(queryset, many=True)
            for index, office_instance in enumerate(queryset):
                serializer.data[index]['worker_count'] = services.get_office_worker_count(office_instance)
                company_pk = serializer.data[index]['office_company']
                serializer.data[index]['office_company'] = services.get_office_company_data(pk=company_pk)
            return Response(serializer.data)
        if isinstance(pk, int):
            obj = get_object_or_404(Office, pk=pk)
            serializer = OfficeSerializer(obj, many=False)
            serializer_data = serializer.data.copy()
            company_pk = serializer_data['office_company']
            serializer_data['office_company'] = services.get_office_company_data(company_pk)
            serializer_data['worker_count'] = services.get_office_worker_count(office_instance=obj)
            serializer_data['workers'] = services.get_office_worker_serialized(obj)
            return Response(serializer_data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class OfficeCreateView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)


