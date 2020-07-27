from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(CategoryDishes)
admin.site.register(SubDishes)
admin.site.register(Dishes)
admin.site.register(Articles)