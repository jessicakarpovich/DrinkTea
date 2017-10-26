from django.shortcuts import render
from .models import Tea
from django.views import generic
# Create your views here.

# current content is only for testing
def index(request):
    
    return render(request, 'index.html')

class TeaListView(generic.ListView):
    model = Tea
    context_object_name = 'tea_list'

class TeaDetailView(generic.DetailView):
    model = Tea
