from datetime import timezone

from django.http import request, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views import View

from .models import *


class MainListView(ListView):
    template_name = 'dishes/dishes_list.html'
    queryset = Dishes.objects.all()


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
        return HttpResponse('Страница корзины в разработке')


class MainLoginView(ListView):
    def get(self, reqest):
        return HttpResponse("Страница автлоризации в разработке")
