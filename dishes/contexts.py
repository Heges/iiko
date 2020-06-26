from .models import CategoryDishes, SubDishes


def category_dishes_list(request):
    return {'categorydishes_list': CategoryDishes.objects.all()}

def subdishes_list(request):
    return {'subdishes_list' : SubDishes.objects.all()}