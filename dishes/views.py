from django.views.generic import ListView, DetailView

from .models import *


class MainListView(ListView):
    template_name = 'dishes/dishes_list.html'
    queryset = Dishes.objects.all()




class MainDetailView(DetailView):
    model = Dishes
    template_name = 'dishes/detail.html'
    slug_field = 'url'


