# Generated by Django 3.0.7 on 2020-06-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_remove_categorydishes_sub_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='slug',
            field=models.SlugField(default='dishes', max_length=150),
            preserve_default=False,
        ),
    ]
