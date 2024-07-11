
from django.urls import path

from . import views


urlpatterns = [
    path('doctor_dash', views.doctorhome, name='doctor'),
    path('patientreport', views.patientrepo, name='patientreport'),
    path('paitentlist/<int:id>', views.patient_list, name='plist'),
]