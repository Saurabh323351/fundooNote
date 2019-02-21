# Generated by Django 2.1.5 on 2019-02-06 04:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0004_auto_20190131_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='collaborate',
            field=models.ManyToManyField(blank=True, related_name='collaborated_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
