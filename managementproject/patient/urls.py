from django.urls import path
from . import views
urlpatterns = [
    path('patienthome',views.patient,name='patient')
]