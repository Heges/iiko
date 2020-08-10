import json

import simplejson as simplejson
from PIL.SpiderImagePlugin import isInt
from django.contrib.auth import login, authenticate
from django.core.exceptions import ObjectDoesNotExist
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
            return render(request, 'dishes/index.html')

    def get_context_data(self, **kwargs):
        context = super(MainListView, self).get_context_data(**kwargs)
        context['dishes_list'] = Dishes.objects.all().order_by('-id')[:3]
        context['articles_list'] = Articles.objects.all().order_by('-id')[:3]
        context['form'] = SearchForm()
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
        obj = Dishes.objects.get(id=request.POST['id'])
        product = get_object_or_404(Dishes, id=obj.id)
        cart = Cart(request)
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


class MainArticles(View):

    def get(self, request):
        articles_list = Articles.objects.all()
        return render(request, 'dishes/articles.html', {'articles_list': articles_list})

    def post(self, request):
        name = request.POST['id']
        data = list(Articles.objects.values().filter(id=name))
        return JsonResponse(data, safe=False)


class MainArticlesDetail(View):

    def get(self, request, pk):
        articles_detail = Articles.objects.filter(id=pk)
        return render(request, 'dishes/articles_detail.html', {'articles_detail': articles_detail})


class MainArticlesCreate(View):
    pass


class MainArticlesChange(TemplateView):
    template = 'dishes/articles_change.html'

    def post(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            id_articles_for_like = request.POST['id']

            return HttpResponse('Uraaaa')

    def get_context_data(self, **kwargs):
        context = super(MainArticlesChange, self).get_context_data(**kwargs)
        return context


class MainVotesView(View):
    model = None
    vote_type = None

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id,
                                                  user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                'result': result,
                'like_count': obj.votes.likes().count(),
                'dislike_count': obj.votes.dislikes().count(),
                'sum_rating': obj.votes.sum_rating()

                }
            ), content_type='application/json'
        )

