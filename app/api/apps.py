"""
App configure file
"""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Api app configure class ApiConfig extends AppConfig
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
