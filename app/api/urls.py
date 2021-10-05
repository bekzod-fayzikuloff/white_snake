"""
Api routes(urls) file
"""
from rest_framework import routers
from django.urls import path
from . import views
from . import viewsets

app_name: str = "api"

router = routers.DefaultRouter()
router.register(r"company", viewsets.CompanyViewSet)
router.register(r"person", viewsets.PersonViewSet)
router.register(r"language", viewsets.LanguageViewSet)

urlpatterns = [
    path("office/", views.OfficeView.as_view()),
    path("office/<int:pk>", views.OfficeView.as_view()),
    path("office/create/", views.OfficeCreateView.as_view()),
]

urlpatterns += router.urls
