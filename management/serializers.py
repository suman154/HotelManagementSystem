from rest_framework import serializers
from .models import RoomType, Room, User


class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ['email', 'password']

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
