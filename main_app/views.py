from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

# Create your views here.
def meds_index(request):
  return render(request, 'meds/index.html')
#   return render(request, 'meds/index.html', { 'meds': meds })