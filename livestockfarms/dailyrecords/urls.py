from django.urls import path
from . import views


urlpatterns = [
    # livestockrecords
    path('', views.daily_home, name = "daily-home"),
    path('daily-feeding/<str:pk>/', views.feeding_add, name = "daily-feeding"),
    
    
    
    ]