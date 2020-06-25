from django.shortcuts import render
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, request
from .models import *
# Create your views here.

def IndexView(ListView):
    #model = Dishes
    #queryset = Dishes.objects.all()
    #context = {'disheslist': disheslist}
    #return context()
    disheslist = Dishes.objects.all()
    template = loader.get_template('dishes/base.html')
    context = {'disheslist': disheslist}
    return HttpResponse(template.render(context))


class DetailView(DetailView):
    model = Dishes
    queryset = Dishes.objects.all()
    template_name = 'dishes/detail.html'

    """def get(self, request):
        model = Dishes
        queryset = Dishes.objects.all()
        return render(request, 'dishes/base.html', {'dishes_list':queryset})"""

