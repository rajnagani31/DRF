from .models import nastahouse
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .serializer import NastahouseSerializer
from rest_framework.response import Response   
from rest_framework import status 


class NastahouseCreateView(CreateAPIView):
    queryset = nastahouse.objects.all()
    serializer_class = NastahouseSerializer

class NastahouseListView(ListAPIView):
    queryset = nastahouse.objects.all()
    serializer_class = NastahouseSerializer

    def get(self,request):
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