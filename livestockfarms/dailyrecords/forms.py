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
            'livestock': forms.HiddenInput(),
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
             'livestock':'',
            'datepurchased': '',
            'medication': '',
            'disease': '',
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