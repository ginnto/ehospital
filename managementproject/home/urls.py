from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index')   #path(urlname,function calling,name of the path

]

