from django.shortcuts import render, redirect
from .models import *
from .serializations import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# class Company_View(APIView):

#     def get(self, request):
#         companyData = Mobile_Company.objects.all()
#         return Response({'companydata': companyData})


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
