from django.db import models

# Create your models here.
from django.urls import reverse


class Dishes(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    image = models.ImageField('Image', null=True, blank=True)
    ccal = models.PositiveIntegerField('Калорийность', default=0)
    """текстовое поле белков углеводов и жиров, руками пусть вводят нефиг калькуляторы """
    pfc = models.CharField(max_length=100)
    weight = models.PositiveIntegerField('Вес в граммах', default=0)
    price = models.PositiveIntegerField('Цена', default=0)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def get_absolute_url(self):
        return reverse('dishes:detail', kwargs={"pk": self.id})

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




