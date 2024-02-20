from django.urls import path
from .views import RoomTypeView

urlpatterns = [
    path('room-type/', RoomTypeView.as_view({'get':'list', 'post':'create'})),
]