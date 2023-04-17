from django.shortcuts import render, redirect
from .models import Med
from .forms import WhenTakenForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Add the following import
from django.http import HttpResponse

class MedCreate(LoginRequiredMixin, CreateView):
  model = Med
  fields = ['name', 'quantity', 'perscribed', 'expiration', 'instructions']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class MedUpdate(LoginRequiredMixin, UpdateView):
  model = Med
  fields = '__all__'

class MedDelete(LoginRequiredMixin, DeleteView):
  model = Med
  success_url = '/meds/'
# Define the home view

def home(request):
  return render(request, 'home.html')

# Create your views here.
@login_required
def meds_index(request):
  meds = Med.objects.filter(user=request.user)
  return render(request, 'meds/index.html', { 'meds': meds })

@login_required
def meds_detail(request, med_id):
  med = Med.objects.get(id=med_id)
  whentaken_form = WhenTakenForm()
  return render(request, 'meds/detail.html', { 'med': med, 'whentaken_form': whentaken_form})

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
