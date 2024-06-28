from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    obj = Doctors.objects.all()
    return render(request,'index.html',{'var':obj})


