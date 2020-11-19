from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FarmName)
admin.site.register(Livestockname)
admin.site.register(Livestock)
admin.site.register(Addmedication)
admin.site.register(Adddisease)
admin.site.register(Mortality)
admin.site.register(Medication)
admin.site.register(Feeding)
