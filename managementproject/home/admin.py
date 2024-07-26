from django.contrib import admin
from .models import *
# Register your models here.

class docadmin(admin.ModelAdmin):
    list_display = ['name','contact']
    list_editable = ['contact']
admin.site.register(Doctors,docadmin)    #admin.site.register(modelname)


class deptadmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Department,deptadmin)


class ptadmin(admin.ModelAdmin):
    list_display = ['name','Address','Contact','Symptoms','Doctor','Status']
    list_editable = ['Address','Contact','Symptoms','Doctor','Status']
admin.site.register(Patients,ptadmin)







