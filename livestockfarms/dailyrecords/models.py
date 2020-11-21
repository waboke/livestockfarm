from django.db import models
from livestockrecords.models import Livestock

# Create your models here.
class Addmedication(models.Model):
    MEDICATIONTYPE = (
        ('Drugs', 'Drugs'),
        ('Vaccination', 'Vaccination'),
        
    )
    name = models.CharField(max_length=200, null=True)
    medicationType = models.CharField(max_length=200, null=True, choices= MEDICATIONTYPE)

    def __str__(self):
        return self.name

class Adddisease(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
    

class DailyRecords(models.Model):  
    livestock = models.ForeignKey(Livestock, null=True, on_delete = models.SET_NULL)  
    dateAdded =models.DateTimeField(auto_now_add=True, null=True)
    datepurchased=models.DateField(auto_now_add=False, null=True)

    class Meta:
        abstract = True

class Mortality(DailyRecords):
    qty = models.IntegerField()
    cause = models.TextField(null=True)

class Medication(DailyRecords):
     medication = models.ForeignKey(Addmedication, null=True, on_delete = models.SET_NULL) 
     disease = models.ForeignKey(Adddisease, null=True, on_delete = models.SET_NULL)  
   
class Feeding(DailyRecords):
    feedname = models.CharField(max_length=200, null=True)
    qty = models.FloatField()
