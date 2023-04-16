from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
class Med:
  def __init__(self, name, quantity, perscribed, expiration, instructions):
    self.name = name
    self.quantity = quantity
    self.perscribed = perscribed
    self.expiration = expiration
    self.instructions = instructions
meds = [
  Med('Adderall', 20, '10/11/12', '10/11/14', '5 mg orally 1 or 2 times a day'),
  Med('Zyrtec', 20, '10/11/12', '10/11/14', '5 mg orally 1 or 2 times a day'),
]
# Define the home view
def home(request):
    return render(request, 'home.html')

# Create your views here.
def meds_index(request):
#   return render(request, 'meds/index.html')
  return render(request, 'meds/index.html', { 'meds': meds })