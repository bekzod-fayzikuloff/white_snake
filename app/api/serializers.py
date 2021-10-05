"""
There made SerializerClass for serializing model instance data to JSON
"""
from rest_framework import serializers
from .models import Company, Office, Person, Language


class CompanySerializer(serializers.ModelSerializer):
    """
    CompanySerializer extends ModelSerializer
    This class realize Company model serializing
    and choice all model field for serialize
    """

    class Meta:
        """
        CompanySerializer Metaclass
        """
        model = Company
        fields = "__all__"


class OfficeSerializer(serializers.ModelSerializer):
    """
    CompanySerializer extends ModelSerializer
    This class realize Company model serializing
    and choice all model field for serialize
    """

    class Meta:
        """
        CompanySerializer Metaclass
        """
        model = Office
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    """
    CompanySerializer extends ModelSerializer
    This class realize Company model serializing
    and choice all model field for serialize
    """

    class Meta:
        """
        CompanySerializer Metaclass
        """
        model = Person
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    """
    CompanySerializer extends ModelSerializer
    This class realize Company model serializing
    and choice all model field for serialize
    """

    class Meta:
        """
        CompanySerializer Metaclass
        """
        model = Language
        fields = "__all__"
