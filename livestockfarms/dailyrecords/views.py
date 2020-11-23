from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from livestockrecords.models import *
from .models import *
from .forms import *

# Create your views here.

def daily_home(request):
    context =()
    template = 'dailyrecords/daily_home.html'
    return render(request, template, context)

def save_feeding_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            livestocks = Livestock.objects.all() 
            feeds = livestocks.feeding_set.all()
            context ={
                'feeds': feeds
            }
            data['html_livestock_list'] = render_to_string('includes/_list_feeding.html', context)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def livestocks_details(request, pk):
    livestocksDetails = Livestock.objects.get(id=pk) 
    feeds = livestocksDetails.feeding_set.all() 
    medication = livestocksDetails.medication_set.all() 
    mortality = livestocksDetails.mortality_set.all() 
    if request.method == 'POST':
        feed_form = FeedingForm(request.POST ,initial={'livestock': pk})
        mort_form = mortalityForm(request.POST ,initial={'livestock': pk})
        med_form = MedicationForm(request.POST ,initial={'livestock': pk})
        if feed_form.is_valid():
                feed_form.save()

        elif mort_form.is_valid():
            mort_form.save()
            
        elif med_form.is_valid():
            med_form.save()
            
        return redirect('livestock-details', pk = pk )
        
    else:
        feed_form = FeedingForm(initial={'livestock': livestocksDetails})
        mort_form = mortalityForm(initial={'livestock': livestocksDetails})
        med_form = MedicationForm(initial={'livestock': livestocksDetails})
        context ={'livestocksDetails':livestocksDetails, 'feeds':feeds,'medication':medication, 'mortality':mortality,'feed_form':feed_form, 'mort_form':mort_form, 'med_form':med_form }
        template ='dailyrecords/livestockrecords_details.html'
        return render(request, template,context)
    
   
def drugs_view(request):
    drugs = Addmedication.objects.all()
    disease = Adddisease.objects.all()
    if request.method == 'POST':
        form =DrugForm(request.POST)
        form =DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drugs')
    else:
        form = DrugForm()
        context = {'drugs':drugs, 'form':form }
        return render(request, 'dailyrecords/drugs_view.html', context )

def disease_view(request):
    disease = Adddisease.objects.all()
    if request.method == 'POST':
        form =DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease')
    else:
        form = DiseaseForm()
        context = {'disease':disease , 'form':form }
        return render(request, 'dailyrecords/disease_view.html', context )
       