from django.urls import path
from . import views


urlpatterns = [
    # livestockrecords
    path('', views.daily_home, name = "daily-home"),
    path('livestock-details/<str:pk>/', views.livestocks_details, name = "livestock-details"),
    path('drugs/', views.drugs_view, name = "drugs"),
     path('disease/', views.disease_view, name = "disease"),

    
    
    
    ]