from django.shortcuts import render

# Create your views here.

def livestocks_home(request):
    context ={}
    return render(request, 'livestockrecords/livestockrecords_index.html', context)