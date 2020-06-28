from .models import CategoryDishes, SubDishes


def category_dishes_list(request):
    return {'categorydishes_list': CategoryDishes.objects.all(), 'categorydishes_filter_list': CategoryDishes.objects.filter(subdishes__subdishes='3')}

