# Generated by Django 3.0.7 on 2020-08-03 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0011_articles_likedone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Thumbslike',
        ),
    ]
