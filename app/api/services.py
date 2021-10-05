"""
Layer for hide some action outside views and viewsets
"""
from rest_framework.utils.serializer_helpers import ReturnDict
from .serializers import CompanySerializer, PersonSerializer, LanguageSerializer
from .models import Office, Company, Language


def get_office_worker_count(office_instance: Office) -> int:
    """
    getting Office model instance
    and return this instance `worker count`
    :param office_instance:
    :return:
    """
    return office_instance.worker.count()


def get_office_company_data(id_: int) -> ReturnDict:
    """
    Serialize Company model record and return JSON
    :param id_:
    :return:
    """
    company_instance = Company.objects.get(pk=id_)
    serializer = CompanySerializer(company_instance)
    return serializer.data


def get_office_worker_serialized(office_instance: Office) -> list:
    """
    Getting Office model record and return list[] with serialized
    workers queryset
    :param office_instance:
    :return:
    """
    workers_queryset = office_instance.worker.all()
    workers = []
    for worker in workers_queryset:
        serialized = PersonSerializer(worker)
        workers.append(serialized.data)
    return workers


def get_person_language_data(id_: int) -> ReturnDict:
    """
    Return Serialized Language model instance
    :param id_:
    :return:
    """
    company_instance = Language.objects.get(pk=id_)
    serializer = LanguageSerializer(company_instance)
    return serializer.data
