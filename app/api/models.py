"""
Declaration all need for us table on database
with DjangoORM
"""
from django.db import models
from django_countries.fields import CountryField


class Company(models.Model):
    """
    Company model field declaration
    """

    name = models.CharField("Company name", max_length=255)
    description = models.TextField("Company description")
    country = CountryField("Company country", blank_label="Select country", blank=True)
    email = models.EmailField("Company email", unique=True, max_length=120)
    phone = models.CharField("Company phone", max_length=15)
    partners = models.ManyToManyField("self", verbose_name="Partners", blank=True)
    is_active = models.BooleanField("Company is active", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Office(models.Model):
    """
    Office model field declaration
    """

    name = models.CharField("Office name", max_length=255)
    description = models.TextField("Office description")
    location = models.CharField("Office location", max_length=255)
    phone = models.CharField("Phone number", max_length=15)
    email = models.EmailField("Email address", unique=True, max_length=120)
    office_company = models.ForeignKey(
        Company, verbose_name="Office company", on_delete=models.CASCADE
    )
    is_active = models.BooleanField("Office is active", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Person(models.Model):
    """
    Person model field declaration
    """

    POSITIONS = [
        ("JR", "Junior"),
        ("MD", "Middle"),
        ("SR", "Senior"),
    ]

    first_name = models.CharField("Firstname", max_length=50)
    last_name = models.CharField("Lastname", max_length=50)
    patronymic = models.CharField("Patronymic", max_length=50)
    date_of_birth = models.DateField("Date of birth")
    position = models.CharField(max_length=2, choices=POSITIONS)
    work_place = models.ManyToManyField(Office, related_name="worker")
    skill = models.CharField("Skill", max_length=120)
    language = models.ManyToManyField("Language")

    def __str__(self) -> str:
        return f"{self.first_name}"


class Language(models.Model):
    """
    Language model field declaration
    """

    name = models.CharField("Language name", max_length=50)
    description = models.TextField("Language description")

    def __str__(self) -> str:
        return f"{self.name}"
