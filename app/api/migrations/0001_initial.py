# Generated by Django 3.0 on 2021-10-03 01:02

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Company name")),
                ("description", models.TextField(verbose_name="Company description")),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, verbose_name="Company country"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=120, unique=True, verbose_name="Company email"
                    ),
                ),
                (
                    "phone",
                    models.CharField(max_length=15, verbose_name="Company phone"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Company is active"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Language name")),
                ("description", models.TextField(verbose_name="Language description")),
            ],
        ),
        migrations.CreateModel(
            name="Office",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Office name")),
                ("description", models.TextField(verbose_name="Office description")),
                (
                    "location",
                    models.CharField(max_length=255, verbose_name="Office location"),
                ),
                ("phone", models.CharField(max_length=15, verbose_name="Phone number")),
                (
                    "email",
                    models.EmailField(
                        max_length=120, unique=True, verbose_name="Email address"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Office is active"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "office_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Company",
                        verbose_name="Office company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="Firstname"),
                ),
                ("last_name", models.CharField(max_length=50, verbose_name="Lastname")),
                (
                    "patronymic",
                    models.CharField(max_length=50, verbose_name="Patronymic"),
                ),
                ("date_of_birth", models.DateField(verbose_name="Date of birth")),
                (
                    "position",
                    models.CharField(
                        choices=[("JR", "Junior"), ("MD", "Middle"), ("SR", "Senior")],
                        max_length=2,
                    ),
                ),
                ("skill", models.CharField(max_length=120, verbose_name="Skill")),
                ("language", models.ManyToManyField(to="api.Language")),
                (
                    "work_place",
                    models.ManyToManyField(related_name="worker", to="api.Office"),
                ),
            ],
        ),
    ]
