from .cart import Cart
from .models import CategoryDishes, SubDishes, Dishes


def category_dishes_list(request):
    return {'categorydishes_list': CategoryDishes.objects.all()}


def cart(request):
    return {'cart': Cart(request)}

