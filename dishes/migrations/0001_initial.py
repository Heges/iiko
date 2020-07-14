# Generated by Django 3.0.7 on 2020-06-24 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=600)),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('ccal', models.PositiveIntegerField(default=0, verbose_name='Калорийность')),
                ('proteins', models.PositiveIntegerField(default=0, verbose_name='Белки')),
                ('fats', models.PositiveIntegerField(default=0, verbose_name='Жиры')),
                ('carbohydrates', models.PositiveIntegerField(default=0, verbose_name='Углеводы')),
                ('weight', models.PositiveIntegerField(default=0, verbose_name='Вес в граммах')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='SubDishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('dishes', models.ManyToManyField(related_name='dishes', to='dishes.Dishes', verbose_name='блюдо')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='CategoryDishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('sub_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.SubDishes')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
