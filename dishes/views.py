from datetime import timezone

from django.http import request, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views import View

from .models import *


class MainListView(ListView):
    template_name = 'dishes/dishes_list.html'

    def get_queryset(self):
        return Dishes.objects.all().order_by('-id')[:4]


class MainDetailView(DetailView):
    model = Dishes
    template_name = 'dishes/detail.html'


class MainCategoryDishes(View):
    def get(self, request, slug):
        if slug:
            menu_list = CategoryDishes.objects.filter(slug=slug)
            submenu_list = SubDishes.objects.filter(slug=slug)
            return render(request, 'dishes/categorydishes.html', {'menu_list': menu_list, 'submenu_list': submenu_list})


class MainCartView(ListView):

    def get(self, reqest):
        return render(reqest, 'cart/cart.html')


class MainLoginView(ListView):

    def get(self, reqest):
        return render(reqest, 'login/login.html')


class MainRegistrView(ListView):

    def get_context_object_name(self, object_list, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, reqest):
        return render(reqest, 'login/registr.html')
