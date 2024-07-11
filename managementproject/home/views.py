from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    obj = Doctors.objects.all()

# --------------------------------------------
    var = Paginator(obj,1)
    pgnum =int(request.GET.get('page',1))
    try:
        doc = var.page(pgnum)
    except(InvalidPage,EmptyPage):
        doc = var.page(var.num_pages)
# ----------------------------------------------

    return render(request,'index.html',{'var':obj})
import math


