from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import UserTicketSerializer , StudentSerializer ,BookOrderSerializer
from .models import UserTicket , Student , Product ,BookOrder
from rest_framework.response import Response
from rest_framework import status
# Create your views here.`

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def UserTicketAPI(request , pk=None):
    if request.method == 'GET':
        if pk:      
            user = UserTicket.objects.filter(id=pk).exists()
            if user :
                    data = UserTicket.objects.values('id','first_name')
                    # serializer = UserTicketSerializer(data ,many=True)
                    return Response({
                        # "data":serializer.data,
                        "data":data,
                        "status": status.HTTP_200_OK
                    })
                
            return Response({
                        "error":"error",
                        "status":status.HTTP_400_BAD_REQUEST
                    })
    elif request.method == 'POST':
        serializer = UserTicketSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Data":"Your Ticket Booked Success Fully"},status.HTTP_201_CREATED)
        return Response({"error":serializer.errors},status.HTTP_404_NOT_FOUND)
    


    elif request.method == 'PATCH':
        if pk:
            user = UserTicket.objects.filter(pk=pk).exists()
            if user:
                try:
                    instance = UserTicket.objects.get(pk=pk)   
                    serializer = UserTicketSerializer(instance ,data = request.data, partial=True) 
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"Data":"Your Ticket Updated Success Fully"},status.HTTP_200_OK)
                    return Response({"error":serializer.errors},status.HTTP_404_NOT_FOUND)  
                except UserTicket.DoesNotExist:
                    return Response({"error":"Data Not Found"},status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        if pk:
            user = UserTicket.objects.filter(pk=pk).exists()
            if user:
                user = UserTicket.objects.get(pk=pk)
                user.delete()
                return Response({"Data":"Your Ticket Deleted Success Fully"},status.HTTP_204_NO_CONTENT)
            return Response({"error":"Data Not Found"},status.HTTP_404_NOT_FOUND)
        return Response({"error":"ID Not Found"},status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def GetStudentData(request ,pk):
    if request.method == 'GET':
        user = Student.objects.filter(pk=pk).exists()
        if user:
            instance = Student.objects.get(id=pk)
            serializer = StudentSerializer(instance)
            print(serializer.data)                
            return Response(
                {
                    "status":status.HTTP_200_OK,
                    "data":serializer.data
                }
            )
        return Response({"ERROR":"User Does not exsist"} , status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def Products(request,pk):
    if pk:
        user = Product.objects.filter(pk=pk).exists()
        if user:
            data = Product.objects.filter(user='a')
            all_data = data.values('order').all()
            print(all_data)
            return HttpResponse("ok")
            # serializer = StudentSerializer(user)

@api_view(['GET'])
def GetUserItemsData(request,pk):
    # customer_name = request.query_params.get('Customer_name_id')            
    # print(customer_name)
    book_items = BookOrder.objects.filter(Customer_name_id=pk).values('Items_id').all()
    serializer = BookOrderSerializer(book_items,many=True)
    print(serializer.data)
    print(book_items)
    return Response({
        "data":serializer.data,
        "status":status.HTTP_200_OK
    
        })