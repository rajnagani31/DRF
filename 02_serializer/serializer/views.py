from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework import status
from .serializer import CompanydataSerializer, companySerializer
from .models import company, Companydata
# Create your views here.
class CompanyView(APIView):
    def post(self, request):

        serializer = companySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def get(self,request,pk=None):
        # data = company.objects.all().filter(pk=pk)
        if pk:
            print("yes")
            data = company.objects.filter(id=pk)
            serializer = companySerializer(data, many=True)
        else:
            print("ok")
            return Response({"message": "Please provide a valid ID"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = companySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CompanyDataView(APIView):
    def post(self,request):
        ser = CompanydataSerializer(data = request.data)
        
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED) 
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)  

    def get(self,request,pk=None):
        if pk:
            data = Companydata.objects.filter(company_id=pk)
            serializer = CompanydataSerializer(data, many=True)
        
        else:
            return Response({"message": "please provide a valid ID"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
                    
            
    def put(self,request,pk=None):
        if pk:
            try:

                data = Companydata.objects.get(id=pk)
                serializer = CompanydataSerializer(data,data = request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"ok","data":serializer.data},status=status.HTTP_200_OK)
                
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
            except Companydata.DoesNotExist:
                return Response({"message":"Data Note Found"},status=status.HTTP_404_NOT_FOUND)

