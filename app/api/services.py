from .serializers import CompanySerializer, PersonSerializer
from .models import Office, Company


def get_office_worker_count(office_instance: Office) -> int:
    return office_instance.worker.count()


def get_office_company_data(pk: int):
    company_instance = Company.objects.get(pk=pk)
    serializer = CompanySerializer(company_instance)
    return serializer.data


def get_office_worker_serialized(office_instance: Office):
    workers_queryset = office_instance.worker.all()
    workers = []
    for worker in workers_queryset:
        serialized = PersonSerializer(worker)
        workers.append(serialized.data)
    return workers
