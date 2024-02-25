from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import RoomType,Room,User
from .serializers import RoomTypeSerializer, RoomSerializer, UserSerializer
from rest_framework.response import Response

def list(self,request):
    pass

# Create your views here.
class RoomTypeView(ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomView(GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


def get(self,request):
    Room_objs = self.get_queryset()
    serializer = self.serializer_class(Room_objs,many=True)
    return Response(serializer.data)


def post(self,request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

class RoomEditView(GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


    def get(self,request,pk):
        room_obj = Room.objects.get(id=pk)
        seriaizer = RoomSerializer(room_obj)
        return Response(seriaizer.data)


    def put(self,request,pk):
        room_obj = Room.objects.get(id=pk)
        serializer = RoomSerializer(room_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

    def delete(self,request,pk):
        room_obj = Room.objects.get(id=pk)
        room_obj.delete()
        return Response("Data Deleted")
    

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def register(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response('user created')
        else:
            return Response(serializer.errors)
        
    def login(self,request):
        pass