from django import forms
from django.forms import ModelForm
from .models import *

class LivestocksForm(ModelForm):
    
    class Meta:
        model = Livestock
        fields = ('farmName','livestockname', 'qty', 'datepurchased',)
        
        labels = {
            'farmName': 'Farm Name',
            'livestockname': 'Live Stock Type',
            'qty': 'Quantity ',
            'datepurchased': 'Date ',
        }
        widgets = {
            
            'farmName':forms.Select( attrs={
                'placeholder': 'Select farm *',
                'class': 'form-control',
                
                }),
            'livestockname':forms.Select(attrs = { 
                'placeholder': 'Select Product *',
                'class': 'form-control'}),
            'qty':forms.TextInput(attrs = { 
                'placeholder': 'Quantity of Product *',
                'class': 'form-control'}),
            'datepurchased':forms.TextInput(attrs = { 
                'placeholder': 'Date of purchase *',
                'class': 'form-control',
                'type': 'date',}),
                
        }
class FarmNameForm(ModelForm):
    class Meta:
        model = FarmName
        fields = ('name','Phone', 'address', 'city', 'state',)

        labels = {
            'name': 'Farm Name',
            'Phone': 'Phone Number',
            'address': 'Farm Address ',
            'city': 'City  ',
            'state': 'State  ',
        }
        widgets = {
            'name':forms.TextInput(attrs = { 
                'placeholder': 'Name of farm *',
                'class': 'form-control'}),
            'Phone':forms.TextInput(attrs = { 
                'placeholder': 'Phone Number *',
                'class': 'form-control'}),
            'address':forms.TextInput(attrs = { 
                'placeholder': 'Farm address*',
                'class': 'form-control'}),
            'city':forms.TextInput(attrs = { 
                'placeholder': 'farm Twon *',
                'class': 'form-control'}),
            'state':forms.TextInput(attrs = { 
                'placeholder': 'Farm state *',
                'class': 'form-control'}),
                
        }

class livestocknameForm(ModelForm):
    class Meta:
        model = Livestockname
        fields = ('name','description',)

        labels = {
            'name': 'Livestock Type',
            'description': 'Description',
            
        }
        widgets = {
            'name':forms.TextInput(attrs = { 
                'placeholder': 'Type *',
                'class': 'form-control'}),
            'description':forms.Textarea(attrs = { 
                'placeholder': 'Little description *',
                'class': 'form-control'}),
            
                
        }
