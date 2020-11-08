# Shreyas

commands flow to create project:
1] In terminal create Project using following command
        django-admin startproject Project

2] Goto the project create App using following command in terminal:
        py manage.py startapp Mobile

3] Goto the Project/settings.py file and write inside 
        INSTALLED_APPS = [
             'Mobile.apps.MobileConfig',
             'rest_framework',
        ]

  
4] Write the Model inside module.py file:

 from django.db import models

# Create your models here.


class Mobile_Company(models.Model):
    company_id = models.AutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=32)
    is_indian = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Mobile_Model(models.Model):
    company = models.ForeignKey(Mobile_Company, on_delete=models.CASCADE)

    def number():
        no = Mobile_Model.objects.count()
        comapnyName = Mobile_Company.objects.filter(company_id=1)
        if no == None:
            return comapnyName[0].company_name[0] + str(1)
        else:
            return comapnyName[0].company_name[0] + str(no + 1)

    model_id = models.AutoField(
        primary_key=True, unique=True)
    model_name = models.CharField(max_length=32)

    internal_id = models.CharField(
        max_length=32, default=number)

    def __str__(self):
        return self.model_name


5] Interminal write following command:
    i] py manage.py makemigrations
    ii] py manage.py migrate
    iii] py manage.py creatsuperuser
          username:admin
          password:admin

6] In admin.py file write,
    admin.site.register(Mobile_Company)
    admin.site.register(Mobile_Model)
 
7] Create serializations.py file and write the below code:
  
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

8] Goto the views.py file and write the below code:

      from django.shortcuts import render, redirect
      from .models import *
      from .serializations import *
      from rest_framework.views import APIView
      from rest_framework.response import Response
      from rest_framework import status

      # Create your views here.


      class Company_Create(APIView):

          def get(self, request):
              company = Mobile_Company.objects.all()
              serializer = CompanySerializer(company, many=True)
              return Response(serializer.data)

          def post(self, request):
              serializer = CompanySerializer(data=request.data)
              print(serializer)
              if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
              return Response(serializer.errors)


      class Model_Create(APIView):

          def get(self, request):
              model = Mobile_Model.objects.all()
              serializer = ModelSerializer(model, many=True)
              return Response(serializer.data)

          def post(self, request):
              serializer = ModelSerializer(data=request.data)
              if serializer.is_valid():
                  serializer.save()

                  return Response(serializer.data)
              return Response(serializer.errors)

9] Goto the Project/urls.py file:

      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('mobile/', include('Mobile.urls')),
      ]

10] Create the urls.py file inside the Mobile:

      from django.urls import path, include
      from .views import *

      urlpatterns = [
          path('company', Company_Create.as_view(), name='company-create'),
          path('model', Model_Create.as_view(), name='model-create'),

      ]
