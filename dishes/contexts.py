from .models import CategoryDishes, SubDishes


def category_dishes_list(request):
    return {'categorydishes_list': CategoryDishes.objects.all()}

