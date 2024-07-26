from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
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
    return render(request,'index.html',{'var':doc})

def search(request):
    if 'q' in request.GET:
        query = request.GET.get('q')  #query = 9946
        doc = Doctors.objects.all().filter(Q(name__icontains=query)|Q(contact__icontains=query))
        print(query,doc)

    return render(request,'search.html',{'d':doc})

