# Generated by Django 3.0.7 on 2020-08-03 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dishes', '0012_delete_thumbslike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbslike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_object', to='dishes.Articles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Thumbslike',
                'verbose_name_plural': 'Thumbslikes',
            },
        ),
    ]
