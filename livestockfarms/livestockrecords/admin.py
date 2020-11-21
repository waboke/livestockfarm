from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FarmName)
admin.site.register(Livestockname)
admin.site.register(Livestock)
