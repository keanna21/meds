from django.shortcuts import render, redirect
from .models import Med
from .forms import WhenTakenForm
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
  whentaken_form = WhenTakenForm()
  return render(request, 'meds/detail.html', { 'med': med, 'whentaken_form': whentaken_form})

def add_whentaken(request, med_id):
  # create a ModelForm instance using the data in request.POST
  form = WhenTakenForm(request.POST)
  # check what request.POST is giving us
  # print(request.POST, '<<<request.POST')
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_whentaken = form.save(commit=False)
    new_whentaken.med_id = med_id
    new_whentaken.save()
  return redirect('detail', med_id=med_id)