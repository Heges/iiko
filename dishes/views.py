from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import *
# Create your views here.

def IndexView(ListView):
    model = CategoryDishes
    categoryDishes_list = CategoryDishes.objects.all()
    return HttpResponse('hi')