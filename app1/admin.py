from django.contrib import admin
from app1.models import Financialdata,Analytics
# Register your models here.
from .models import CustomUser  


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Financialdata)
class Financialdata(admin.ModelAdmin):
    list_display = ['acc_id']


@admin.register(Analytics)
class Analytics(admin.ModelAdmin):
    list_display = ['financialdata']





