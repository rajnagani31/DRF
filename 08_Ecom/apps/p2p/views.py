from rest_framework import generics
from rest_framework.views import APIView
from .models import User, Email, product, profile
from rest_framework.response import Response
from .serializers import ProductSerializer
from pydantic import BaseModel, Field

class UserCreateAPIView(APIView):
    def post(self, request):
        username = 'raj'
        email = 'raj@gmail.com'
        password = 'raj123'
        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        user_delete = Email.objects.filter(is_sended= False)
        user_delete.delete()
        return Response({'message': 'User created successfully'})
    
class ProductData(BaseModel):
    name : str
    price : float
    description : str
    data : str | None = None

class ProductDataResponse(BaseModel):
    name : str
    price : float
    description : str
    data : str | None = None
        
class ProductAPIView(APIView):
    def get(self, request):
        products = product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'message': 'Products fetched successfully', 'data': serializer.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        data_validation = ProductData(**request.data)
        print('----------------------',data_validation)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ProductDataResponse(
            name=data_validation.name,
            price=data_validation.price,
            description=data_validation.description,
            data=data_validation.data
        )
        # return Response(response.model_dump(), status=201)
        return Response({'message': 'Product created successfully', 'data': data_validation.model_dump()})




    
