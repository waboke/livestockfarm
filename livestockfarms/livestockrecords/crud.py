from crudbuilder.abstract import BaseCrudBuilder
from .models import *

class LivestockCrud(BaseCrudBuilder):
        model = Livestock
        search_fields = ['livestockname']
        tables2_fields = ('farmName', 'livestockname','qty','datepurchased')
        tables2_css_class = "table table-bordered table-condensed"
        tables2_pagination = 10  # default is 10
        modelform_excludes = ['dateAdded']

class FarmNameCrud(BaseCrudBuilder):
    model =farmName
    search_fields = ['name']
    tables2_fields = ('name', 'phone','address','state', 'city')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 10  # default is 10
    modelform_excludes = ['dateAdded']

class LivestocknameCrud(BaseCrudBuilder):
        model = Livestockname
        search_fields = ['name']
        tables2_fields = ('name', 'description')
        tables2_css_class = "table table-bordered table-condensed"
        tables2_pagination = 10  # default is 10
        modelform_excludes = ['dateAdded']