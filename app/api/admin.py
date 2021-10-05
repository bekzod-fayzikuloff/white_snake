"""
Configure django admin panel for `api` app
"""
from django.contrib import admin
from .models import Company, Office, Person, Language


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    CompanyAdmin Panel
    """
    list_filter = ("name", "is_active")
    list_display = (
        "name",
        "description",
        "phone",
    )


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    """
    Office Admin Panel on admin site
    """


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """
    Person Admin Panel on admin site
    """


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """
    Language Admin Panel on admin site
    """
