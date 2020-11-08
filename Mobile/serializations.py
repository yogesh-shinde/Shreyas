from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile_Company
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mobile_Model
        fields = '__all__'
        read_only_fields = ('internal_id',)
