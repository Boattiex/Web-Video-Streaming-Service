# Generated by Django 2.1.7 on 2019-04-04 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestream',
            name='key',
            field=models.CharField(default=functools.partial(django.utils.crypto.get_random_string, *(20,), **{}), max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
