
from django.urls import path

from . import views


urlpatterns = [
    path('doctor_dash', views.doctorhome, name='doctor')
]