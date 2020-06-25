from django.shortcuts import render
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, request
from .models import *
# Create your views here.

class ListView(ListView):
    model = Dishes
    disheslist = Dishes.objects.all()


class DetailView(DetailView):
    model = Dishes
    template_name = 'dishes/detail.html'
    slug_field = 'url'


