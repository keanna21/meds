from django.db import models
from django.urls import reverse

# Create your models here.
class Med(models.Model):
  name = models.CharField(max_length=100)
  quantity = models.IntegerField()
  perscribed = models.DateField()
  expiration = models.DateField()
  instructions = models.TextField(max_length=250)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'med_id': self.id})