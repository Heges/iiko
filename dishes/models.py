from django.db import models

# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    image = models.ImageField('Image')
    ccal = models.PositiveIntegerField('Калорийность', default=0)
    """НЕ ЗАБЫТЬ ПОМЕНЯТЬ ПРОТЕИНС ФАСТ И  УГЛЕВОДОС НА ФЛОАТ ЧТОБЫ СЧИТАТЬ ККАЛС """
    proteins = models.PositiveIntegerField('Белки', default=0)
    fats = models.PositiveIntegerField('Жиры', default=0)
    carbohydrates = models.PositiveIntegerField('Углеводы', default=0)
    weight = models.PositiveIntegerField('Вес в граммах', default=0)
    price = models.PositiveIntegerField('Цена', default=0)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class SubDishes(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    dishes = models.ManyToManyField(Dishes, verbose_name='блюдо', related_name='dishes')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class CategoryDishes(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




