from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum

from django.urls import reverse
from django.utils import timezone


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
    counts = models.PositiveIntegerField('Количество', default=1)

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
    image = models.ImageField('Image', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def get_absolute_url(self):
        return reverse("dishes:subcategorydishes", kwargs={"slug": self.slug})


class CategoryDishes(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    subdishes = models.ManyToManyField(SubDishes, verbose_name='Подкатегория', related_name='subdishes')
    image = models.ImageField('Image', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse("dishes:categorydishes", kwargs={"slug": self.slug})


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def articles(self):
        return self.get_queryset().filter(content_type__model='article').order_by('-articles__pub_date')


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name='Голос', choices=VOTES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()


class Articles(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=20, null=True, blank=True)
    deception = models.TextField(max_length=800)
    votes = GenericRelation(LikeDislike, related_query_name='articles')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('dishes:articles', kwargs={"pk": self.id})

