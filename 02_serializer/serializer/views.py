from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from rest_framework.response import Response
from rest_framework import status ,generics
from .serializer import CompanydataSerializer, companySerializer ,BookSerializer
from .models import company, Companydata ,BookData
# Create your views here.
class CompanyView(APIView):
    def post(self,request):
            serializer= companySerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Company SuccessFully Created"},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

    def get(self,request,pk=None):
        if pk:
            try:
                data = company.objects.filter(id=pk)
                serializer = companySerializer(data , many = True)
                return Response(serializer.data,status=status.HTTP_200_OK)


            except company.DoesNotExist:
                return Response({"ERROR":"Data Note Found"},status.HTTP_404_NOT_FOUND)
            
        else:
            return Response({"ERROR":"ID Note FOund"},status=status.HTTP_404_NOT_FOUND)    
        

    def put(self,request,pk=None):
        # if pk:
        #     print('pk',pk)
        cheak_id= company.objects.filter(id=pk).exists()
        

        if cheak_id:
            try:
                " get_or_create and get_or_update both method are valid for data update and create for put method "

                # instance ,created= company.objects.get_or_create(pk=pk) 
                instance = company.objects.get(pk=pk) 

                # instance, created = company.objects.update_or_create(pk=pk)
                serializer = companySerializer(instance , data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Data are created you can cheakout in postgers DB"},status.HTTP_200_OK)
                return Response({'error':serializer.errors,'message':"validation Error"},status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'Message':'Data not created'},status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response({"ERROR":"ID note found"},status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None):
        user = company.objects.filter(id=pk)
        if user.exists():
            user.delete()
            return Response({"message":"User hase deleted"},status.HTTP_508_LOOP_DETECTED)
        else:
            return Response({"Message":"this is is node exists!!"},status.HTTP_400_BAD_REQUEST)

class CompanyDataView(APIView):

    def post(self,request):
        serializer = CompanydataSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk = None):
        " This API give only PK(user id) data"
        if pk:
            user= Companydata.objects.filter(id=pk).exists()
            if user:
                try:
                    instance = Companydata.objects.filter(pk=pk)
                    serializer = CompanydataSerializer(instance, many=True)
                    return Response(serializer.data,status.HTTP_200_OK)
                except:
                    serializer.is_valid()   
                    print('yes e')
                    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
                
            return Response({"message":"User Does not exists "},status.HTTP_400_BAD_REQUEST)
        return Response({"ERROR":"ID Note found!!"},status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        " This API give all Comapny data"
        user = Companydata.objects.all()
        serializer = CompanydataSerializer(user , many =True)
        return Response(serializer.data,status.HTTP_200_OK)
    

    def patch(self,request,pk):
        if pk:
            user= Companydata.objects.filter(id=pk).exists()
            if user:
                try:
                    instance = Companydata.objects.get(pk=pk)
                    serializer = CompanydataSerializer(instance , data=request.data , partial=True) # recheak
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data,status.HTTP_200_OK)
                    return Response({"message":"validation are Fiald","message":serializer.errors},status.HTTP_400_BAD_REQUEST)
                except:
                    return Response({"Error":"Data Note found"},status.HTTP_400_BAD_REQUEST)
                
            else:
                return Response({"message":"User Id does not exists"},status.HTTP_400_BAD_REQUEST)   

    def delete(self,request):
        pk = request.query_params.get('id')
        user= Companydata.objects.filter(pk=pk)
        if not user.exists():
                return Response({"message":"user don't exists"},status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response({"message":"User deleted"},status.HTTP_204_NO_CONTENT)

class BookDataAPI(APIView):
    def post(self , request):
        serializer = BookSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        data = BookData.objects.values("title","author","isbn","published_date","price",'read','date_time').all()
        # print(data.get('title'))
        # data= None
        if not data:
            return Response(
                {
                    "Message":"Data Note Found",
                    "status":status.HTTP_404_NOT_FOUND
                }
            )
        return Response(
            {
            "Book Data":data,
            "status":status.HTTP_200_OK 
        }
        )
    