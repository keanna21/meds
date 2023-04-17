from django.forms import ModelForm
from .models import WhenTaken

class WhenTakenForm(ModelForm):
  class Meta:
    model = WhenTaken
    fields = ['date', 'time', 'quantity']