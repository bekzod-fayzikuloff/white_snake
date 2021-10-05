from django.contrib import admin
from .models import Company, Office, Person, Language


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
