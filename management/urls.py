from django.urls import path
from .views import RoomTypeView
from .views import RoomView


urlpatterns = [
    path('room-type/', RoomTypeView.as_view({'get':'list', 'post':'create'})),
    path('room-type/<int:pk>/',RoomTypeView.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
    path('room/',RoomView.as_view({'get':'list', 'post':'create'}))
]