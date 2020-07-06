from datetime import timezone

from django.http import request, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm, AuthUserForm
from django.contrib.auth.models import User

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


class MainLoginView(LoginView):
    template_name = 'login/login.html'
    form_class = LoginUserForm


class MainRegistrView(CreateView):
    model = User
    template_name = 'login/registr.html'
    form_class = AuthUserForm
    success_url = '../'
    success_msg = 'УСПЕШНО ЯБАТЬ'

