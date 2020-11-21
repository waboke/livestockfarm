from django.urls import path
from . import views


urlpatterns = [
    # livestockrecords
    path('', views.daily_home, name = "daily-home"),
    path('daily-feeding/<str:pk>/', views.daily_feeding, name = "daily-feeding"),
    
    
    
    ]