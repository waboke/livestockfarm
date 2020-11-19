from django.urls import path
from . import views


urlpatterns = [
    # livestockrecords
    path('', views.livestocks_home, name = "livestocks-home"),
    path('livestocks-views/', views.livestocks_views, name = "livestocks-views"),
    path('livestocks-add/', views.livestocks_add, name = "livestocks-add"),
    path('edit-livestock/<str:pk>/', views.edit_livestock, name = "edit-livestock"),  
    path('delete-livestock/<str:pk>/', views.delete_livestock, name = "delete-livestock"),  
    path('livestocks-details/<str:pk>/', views.livestocks_details, name = "livestocks-details"), 
    path('feeding-add/', views.feeding_add, name = "feeding-add"), 
    path('farmname-views/', views.farmname_views, name = "farmname-views"),
    path('farmname-add/', views.farmname_add, name = "farmname-add"),
     path('livestocktype-views/', views.livestocktype_views, name = "livestocktype-views"),
    path('livestocktype-add/', views.livestocktype_add, name = "livestocktype-add"),
    
    ]

