# Generated by Django 2.1.5 on 2019-02-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0006_remove_notes_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='note_images/'),
        ),
    ]