from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import RoomType
from .serializers import RoomTypeSerializer

# Create your views here.
class RoomTypeView(ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer