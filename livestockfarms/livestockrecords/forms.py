from django import forms
from django.forms import ModelForm
from .models import *
from bootstrap_modal_forms.forms import BSModalModelForm
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