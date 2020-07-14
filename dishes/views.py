import json
from datetime import timezone

from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import request, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView

from .cart import Cart
from .forms import LoginUserForm, AuthUserForm
from django.contrib.auth.models import User

from .models import *


class MainListView(ListView):
    template_name = 'dishes/index.html'
    #template_name = 'dishes/dishes_list.html'

    def get_queryset(self):
        return Dishes.objects.all().order_by('-id')[:6]


class MainDetailView(View):

    def get(self, request, pk):
        template_name = 'dishes/detail.html'
        product_list = Dishes.objects.filter(id=pk)
        product = get_object_or_404(Dishes, id=pk)
        cart = Cart(request)
        cart.add(item=product)
        return render(request, template_name, context={'product_list': product_list, 'cart': cart})

    def post(self, request, pk):
        if request.method == 'POST':
            alist = Dishes.objects.filter(id=pk)
            model_obj = Dishes.objects.get(id=pk)
            data = serializers.serialize('json', [model_obj])
            struct = json.loads(data)
            data.json.dumps(struct[0])
            return render(request, 'cart/cart.html', {'alist': alist, 'data': data})
        else:
            return redirect('./')


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
    success_url = '../'
    success_msg = '==========================ВЫ ЗАШЛИ АЛО=========================='

    def get_success_url(self):
        return self.success_url


class MainLogoutView(LogoutView):
    next_page = success_url = '../'


class MainRegistrView(CreateView):
    model = User
    template_name = 'login/registr.html'
    form_class = AuthUserForm
    success_url = '../'
    success_msg = '==========================УСПЕШНО ЯБАТЬ=========================='

    """def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username=username, password=password)
        login(self, request, aut_user)
        return form_valid"""

