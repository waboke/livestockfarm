from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import *
from .forms import *


# Create your views here.

def livestocks_home(request):
    context ={}
    return render(request, 'livestockrecords/livestockrecords_index.html', context)
# start Livestock Model CRUD with Ajax abd json
def livestocks_views(request):
    livestocks = Livestock.objects.all()
    context = {'livestocks':livestocks }
    return render(request, 'livestockrecords/livestockrecords_views.html', context)
    
def livestock_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            livestocks = Livestock.objects.all()
            context = {'livestocks': livestocks}
            data['html_product_list'] = render_to_string('includes/_list_livestock.html', context)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def livestocks_add(request):
    if request.method == 'POST':
        form = LivestocksForm(request.POST)
    else:
        form = LivestocksForm()
    return livestock_form(request, form, 'includes/_add_livestock.html')

def edit_livestock(request, pk):
    livestock = get_object_or_404(Livestock, pk=pk)
    if request.method == 'POST':
        form = LivestocksForm(request.POST, instance=livestock)
    else:
        form = LivestocksForm(instance=livestock)
    return livestock_form(request, form, 'includes/_edit_livestock.html')
 
 
def delete_livestock(request, pk):
    livestocks = get_object_or_404(Livestock, pk=pk)
    data = dict()
    if request.method == 'POST':
        livestocks.delete()
        data['form_is_valid'] = True
        livestocks = Livestock.objects.all()
        context= {'livestocks': livestocks}
        data['html_product_list'] = render_to_string('includes/_list_livestock.html', context )
    else:
        context = {'livestocks': livestocks }
        data['html_form'] = render_to_string('includes/_delete_livestock.html', context, request=request)
    return JsonResponse(data)
# end livestock model

# daily Recording of feeding, medication and mortality
def livestocks_details(request, pk):
    livestocksDetails = Livestock.objects.get(id=pk) 
    feeds = livestocksDetails.feeding_set.all() 
    medication = livestocksDetails.medication_set.all() 
    mortality = livestocksDetails.mortality_set.all() 
    context ={'livestocksDetails':livestocksDetails, 'feeds':feeds,'medication':medication, 'mortality':mortality }
    return render(request, 'livestockrecords/livestockrecords_details.html',context)

def daily_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
           
            context = {}
            data['html_product_list'] = render_to_string('includes/_list_feed.html', context)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def feeding_add(request):
    if request.method == 'POST':
        form = FeedingForm(request.POST)     
    else:
        form = FeedingForm()
    return daily_form(request, form, 'includes/_add_feeding.html')

def edit_livestock(request, pk):
    livestock = get_object_or_404(Livestock, pk=pk)
    if request.method == 'POST':
        form = LivestocksForm(request.POST, instance=livestock)
    else:
        form = LivestocksForm(instance=livestock)
    return livestock_form(request, form, 'includes/_edit_livestock.html')
 
 
def delete_livestock(request, pk):
    livestocks = get_object_or_404(Livestock, pk=pk)
    data = dict()
    if request.method == 'POST':
        livestocks.delete()
        data['form_is_valid'] = True
        livestocks = Livestock.objects.all()
        context= {'livestocks': livestocks}
        data['html_product_list'] = render_to_string('includes/_list_livestock.html', context )
    else:
        context = {'livestocks': livestocks }
        data['html_form'] = render_to_string('includes/_delete_livestock.html', context, request=request)
    return JsonResponse(data)
    # end of darily records
def farmname_views(request):
    farmname = FarmName.objects.all()
    paginator = Paginator(farmname, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {'farmname':farmname, 'page_obj':page_obj }
    return render(request, 'livestockrecords/farmname_view.html', context)
    
def farmname_add(request):
    form =FarmNameForm()
    if request.method == "POST":
        form =FarmNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmname-views')
    context ={'form': form}
    return render(request, 'livestockrecords/farmname_add.html',context)

def livestocktype_views(request):
    type = Livestockname.objects.all()
    paginator = Paginator(type, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {'type':type, 'page_obj':page_obj }
    return render(request, 'livestockrecords/livestocktype_view.html', context )
    
def livestocktype_add(request):
    form =livestocknameForm()
    if request.method == "POST":
        form =livestocknameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livestocktype-views')
    context ={'form': form}
    return render(request, 'livestockrecords/livestotype_add.html', context )