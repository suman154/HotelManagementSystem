from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import RoomType,Room
from .serializers import RoomTypeSerializer, RoomSerializer

# Create your views here.
class RoomTypeView(ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer