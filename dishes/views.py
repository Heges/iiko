import json

import simplejson as simplejson
from PIL.SpiderImagePlugin import isInt
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView

from .cart import Cart
from .forms import LoginUserForm, AuthUserForm, SearchForm, ArticlesForm
from django.contrib.auth.models import User

from .models import *


class MainSerchResult(TemplateView):
    template_name = 'dishes/search_result.html'


class MainListView(TemplateView):
    template_name = 'dishes/index.html'

    def post(self, request):
        sf = SearchForm(request.POST)
        if sf.is_valid():
            keyword = sf.cleaned_data['keyword']
            bbd = Dishes.objects.filter(name__icontains=keyword)
            return render(request, 'dishes/search_result.html', {'bbd': bbd})
        else:
            sf = SearchForm()
            return render(request, 'dishes/index.html', {'form': sf})

    def get_context_data(self, **kwargs):
        context = super(MainListView, self).get_context_data(**kwargs)
        context['dishes_list'] = Dishes.objects.all().order_by('-id')[:3]
        context['articles_list'] = Articles.objects.all().order_by('-id')[:2]
        return context


class MainDetailView(View):

    def get(self, request, pk):
        template_name = 'dishes/detail.html'
        product_list = Dishes.objects.filter(id=pk)
        return render(request, template_name, context={'product_list': product_list})

    def post(self, request, pk):
        obj_id = request.POST['id']
        product = get_object_or_404(Dishes, id=pk)
        cart = Cart(request)
        cart.add(item=product, quantity=1, update_quantity=False)
        obj = Dishes.objects.get(id=obj_id)
        result = {
            'name': obj.name,
            'description': obj.description
        }
        return JsonResponse(result, safe=False)


class MainCategoryDishes(View):

    def get(self, request, slug):
        if slug:
            menu_list = CategoryDishes.objects.filter(slug=slug)
            submenu_list = SubDishes.objects.filter(slug=slug)
            return render(request, 'dishes/categorydishes.html', {'menu_list': menu_list, 'submenu_list': submenu_list})


class MainCartRemove(View):

    def get(self, request, key=None, pk=None):
        if key == 'remove':
            self.cart_remove(request, pk)
            return redirect('dishes:cartview')
        else:
            return redirect('dishes:cartview')

    def cart_remove(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Dishes, id=pk)
        cart.remove(product)


class MainCartPlusValue(View):

    def post(self, request):
        print(request.POST)
        a = dict()
        a = {
            'id': request.POST['id'],
            'counts': request.POST['counts']
        }
        product = get_object_or_404(Dishes, id=request.POST['id'])
        cart = Cart(request)
        count = int(request.POST['counts'])
        if count <= 0:
            print('меньше')
            ad = int(product.id)
            MainCartRemove.cart_remove(MainCartRemove, request, pk=ad)
            print('меньше1')
            cart.remove(product)
        cart.add(item=product, quantity=request.POST['counts'], update_quantity=True)
        return JsonResponse(a)


class MainCartView(TemplateView):
    template_name = 'cart/cart.html'
    success_url = 'cart.html'

    def post(self, request):
        obj = Dishes.objects.get(id=request.POST['id'])
        result = {
            'id': obj.id,
            'name': obj.name,
            'quantity': obj.counts
        }
        cart = Cart(request)
        product = get_object_or_404(Dishes, id=obj.id)
        cart.remove(product)
        return JsonResponse(result, safe=False)

    def get_context_data(self, **kwargs):
        context = super(MainCartView, self).get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

    def get_success_url(self):
        return self.success_url


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

    # def form_valid(self, form):
    #     form_valid = super().form_valid(form)
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']
    #     aut_user = authenticate(username=username, password=password)
    #     login(self, request, aut_user)
    #     return form_valid
    #     new_user = RegisterForm(request.POST)
    #     if new_user.is_valid():
    #         new_user.save()
    #         username = new_user.cleaned_data.get('username')
    #         password = new_user.cleaned_data.get('password2')
    #         user = auth.authenticate(username=username, password=password)
    #         auth.login(request, user)
    #         return redirect('../')
    #         else:
    #         return redirect('../login')


class MainArticles(View):

    def get(self, request):
        articles_list = Articles.objects.all()
        return render(request, 'dishes/articles.html', {'articles_list': articles_list})

    def post(self, request):
        name = request.POST['id']
        data = list(Articles.objects.values().filter(id=name))
        return JsonResponse(data, safe=False)


class MainArticlesCreate(View):
    pass
