
from django.urls import path

from . import views


urlpatterns = [
    path('doctor_dash', views.doctorhome, name='doctor'),
    path('patientreport/<int:Id>', views.patientrepo, name='patientreport'),
    path('paitentlist/<int:id>', views.patient_list, name='plist'),
    path('discharge/<int:id>', views.discharge_details, name='discharge_details'),
    path('report/<int:report_id>/', views. doctor_report_view, name='doctor_report'),
]