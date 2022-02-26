from django.urls import path
from . import views

urlpatterns = [
   path('hotels', views.hotel_view.as_view(), name="HotelView")
]