from django.shortcuts import render
from .models import *

# Create your views here.

def livestocks_home(request):
    context ={}
    return render(request, 'livestockrecords/livestockrecords_index.html', context)

def livestocks_views(request):
    livestock = Livestock.objects.all()
    context ={livestock:'livestock'}
    return render(request, 'livestockrecords/livestockrecords_views.html', context)