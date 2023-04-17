from django.urls import path
from . import views

urlpatterns = [
    # home page 
    path('', views.home, name='home'),
    # index page that shows all medications within database
    path('meds/', views.meds_index, name='index'),
    # details page for each mediction
    path('meds/<int:med_id>/', views.meds_detail, name='detail'),
]
