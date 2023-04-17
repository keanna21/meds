from django.contrib import admin
# import your models here
from .models import Med, WhenTaken

# Register your models here.
admin.site.register(Med)
admin.site.register(WhenTaken)