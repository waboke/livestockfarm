from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from livestockrecords.models import *
from .models import *
from .forms import *


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

def feeding_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            livestocks = Livestock.objects.all()
            feed = livestocks.feeding_set.all()
            context = {'feed': feed}
            data['html_product_list'] = render_to_string('includes/_list_feed.html', context)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def feeding_add(request, pk):
    livestocks = Livestock.objects.get(id=pk)
    if request.method == 'POST':
        form = FeedingForm(request.POST, initial={'livestock': pk})
    else:
        form = FeedingForm(initial={'livestock': livestocks})
    return feeding_form(request, form, 'includes/_add_feeding.html')