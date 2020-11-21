from django.shortcuts import render, redirect
from livestockrecords.models import *

from .models import *
from .forms import *

# Create your views here.

def daily_home(request):
    context =()
    template = 'dailyrecords/daily_home.html'
    return render(request, template, context)

def daily_feeding(request , pk):
    livestocks = Livestock.objects.get(id=pk)
    feed = livestocks.feeding_set.all()
    form =FeedingForm(initial={'livestock': livestocks})
    if request.method == "POST":
        #print('printing post:', request.POST)
        form =FeedingForm(request.POST,initial={'livestock': pk} )
        if form.is_valid():
            form.save()
            return redirect('add_dailyrecords', pk = pk )
    context = {'livestocks': livestocks,  'feed':feed,'form': form } 
    return render(request, 'dailyrecords/daily_feeding.html', context)