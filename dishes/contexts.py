from .models import CategoryDishes, SubDishes


def category_dishes_list(request):
    return {'categorydishes_list': CategoryDishes.objects.all(), 'categorydishes_filter_1_list': CategoryDishes.objects.filter(id='5')}

