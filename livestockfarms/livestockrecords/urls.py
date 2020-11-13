from django.urls import path
from . import views


urlpatterns = [
    # livestockrecords
    path('', views.livestocks_home, name = "livestocks-home"),
    
    ]

