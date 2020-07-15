from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView

from .cart import Cart
from .forms import LoginUserForm, AuthUserForm
from django.contrib.auth.models import User

from .models import *


class MainListView(ListView):
    template_name = 'dishes/index.html'

    def get_queryset(self):
        return Dishes.objects.all().order_by('-id')[:6]


class MainDetailView(View):

    def get(self, request, pk):
        template_name = 'dishes/detail.html'
        product_list = Dishes.objects.filter(id=pk)
        return render(request, template_name, context={'product_list': product_list})

    def post(self, request, pk):
        if request.method == 'POST':
            product = get_object_or_404(Dishes, id=pk)
            cart = Cart(request)
            cart.add(item=product)
            return redirect('/cart/')
        else:
            return redirect('./')


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


class MainCartView(TemplateView):
    template_name = 'cart/cart.html'
    success_url = 'cart.html'

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
    # form_valid = super().form_valid(form)
    # username = form.cleaned_data['username']
    # password = form.cleaned_data['password']
    # aut_user = authenticate(username=username, password=password)
    # login(self, request, aut_user)
    # return form_valid"""
