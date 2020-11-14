from django.urls import path
from . import views


urlpatterns = [
    # livestockrecords
    path('', views.livestocks_home, name = "livestocks-home"),
     path('livestocks-views/', views.livestocks_views, name = "livestocks-views"),
    
    ]

