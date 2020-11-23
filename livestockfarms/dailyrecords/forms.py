from django import forms
from django.forms import ModelForm
from .models import *

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['livestock','datepurchased', 'feedname', 'qty']
        
        labels = {
            'livestock':'',
            'datepurchased': '',
            'feedname': '',
            'qty': '',
        }
        widgets = {
        
            'datepurchased':forms.TextInput( attrs={
                'placeholder': 'Date Added *',
                'class': 'form-control',
                'type': 'date',
                }),
            'feedname':forms.TextInput(attrs = { 
                'placeholder': 'feed name *',
                'class': 'form-control'}),
            'qty':forms.TextInput(attrs = { 
                'placeholder': 'Quantity of feed in kg *',
                'class': 'form-control'}),
                
        }
class mortalityForm(ModelForm):
    
    class Meta:
        model = Mortality
        fields = ['livestock','datepurchased', 'qty', 'cause']
        
        labels = {
             'livestock':'',
            'datepurchased': '',
            'qty': '',
            'cause': '',
        }
        widgets = {
            'livestock': forms.HiddenInput(),
            'datepurchased':forms.TextInput( attrs={
                'placeholder': 'Date Added *',
                'class': 'form-control',
                'type': 'date',
                }),
            'cause':forms.TextInput(attrs = { 
                'placeholder': 'Cause of Mortality *',
                'class': 'form-control'}),
            'qty':forms.TextInput(attrs = { 
                'placeholder': 'Number *',
                'class': 'form-control'}),
                
        }
    
class MedicationForm(ModelForm):
    class Meta:
        model = Medication
        fields = ['livestock','datepurchased', 'medication', 'disease']
        
        labels = {
             'livestock':'Livestock ID',
            'datepurchased': 'Date',
            'medication': 'Drug Name',
            'disease': 'Disease',
        }
        widgets = {
             'livestock': forms.HiddenInput(),
            'datepurchased':forms.TextInput( attrs={
                'placeholder': 'Date Added *',
                'class': 'form-control',
                'type': 'date',
                }),
            'medication':forms.Select(attrs = { 
                'placeholder': 'Drug name *',
                'class': 'form-control'}),
            'disease':forms.Select(attrs = { 
                'placeholder': 'Disease Name *',
                'class': 'form-control'}),
                
        }

class DiseaseForm(ModelForm):
    class Meta:
        model = Adddisease
        fields = ('name','description',)

        labels = {
            'name': 'Disease name',
            'description': 'Description',
            
        }
        widgets = {
            'name':forms.TextInput(attrs = { 
                'placeholder': 'isease name *',
                'class': 'form-control'}),
            'description':forms.Textarea(attrs = { 
                'placeholder': 'Little description *',
                'class': 'form-control'}),
            
                
        }
class DrugForm(ModelForm):
    class Meta:
        model = Addmedication
        fields = ('name','medicationType',)

        labels = {
            'name': 'Drug name',
            'medicationType': 'Medication Type',
            
        }
        widgets = {
            'name':forms.TextInput(attrs = { 
                'placeholder': 'Drug name *',
                'class': 'form-control'}),
            
    
            
                
        }

