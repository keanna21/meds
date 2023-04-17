from django.shortcuts import render
from .models import Med
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Add the following import
from django.http import HttpResponse

class MedCreate(CreateView):
  model = Med
  fields = '__all__'

class MedUpdate(UpdateView):
  model = Med
  fields = '__all__'

class MedDelete(DeleteView):
  model = Med
  success_url = '/meds/'
# Define the home view

def home(request):
  return render(request, 'home.html')

# Create your views here.
def meds_index(request):
  meds = Med.objects.all()
  return render(request, 'meds/index.html', { 'meds': meds })

def meds_detail(request, med_id):
  med = Med.objects.get(id=med_id)
  return render(request, 'meds/detail.html', { 'med': med })