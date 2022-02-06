from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
#from rest_framework.validators import UniqueValidator
#from django.contrib.auth.password_validation import validate_password
class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ['name_of_project','elect_consumption','waterconsp','meterread']
