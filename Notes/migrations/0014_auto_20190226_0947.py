# Generated by Django 2.1.5 on 2019-02-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0013_auto_20190226_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='reminder',
            field=models.DateTimeField(blank=True, null=True, verbose_name=['%m-%d-%Y %H:%M %p']),
        ),
    ]