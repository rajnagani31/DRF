from .models import nastahouse
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .serializer import NastahouseSerializer
from rest_framework.response import Response   
from rest_framework import status 


class NastahouseCreateView(CreateAPIView):
    queryset = nastahouse.objects.all()
    serializer_class = NastahouseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message":"data  okoo k ok ok ocreated successfully","data":serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

class NastahouseListView(ListAPIView):
    queryset = nastahouse.objects.all()
    serializer_class = NastahouseSerializer

    def list(self,request): # outher vise get -->> override logic
        data = nastahouse.objects.filter(datetime__year=2024)
        serializer = NastahouseSerializer(data,many=True)
        return Response({"data":serializer.data})

class NastahouseDetailView(RetrieveUpdateAPIView):
    queryset = nastahouse.objects.all()
    serializer_class = NastahouseSerializer
    lookup_field = 'id'  # Change to 'pk' if your model uses the default primary key

class NastahouseUpdateView(DestroyAPIView):
    queryset = nastahouse.objects.all()
    serializer_class = NastahouseSerializer
    lookup_field = 'id'  # Change to 'pk' if your model uses the default primary key    