from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import RoomType,Room
from .serializers import RoomTypeSerializer, RoomSerializer
from rest_framework.response import Response

# Create your views here.
class RoomTypeView(ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


def get(self,request):
    Room_objs = self.get_queryset()
    serializer = self.serializer_class(Room_objs,many=True)
    return Response(serializer.data)