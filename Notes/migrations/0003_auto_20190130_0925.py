# Generated by Django 2.1.5 on 2019-01-30 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_auto_20190130_0651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='remainder',
            new_name='reminder',
        ),
    ]
