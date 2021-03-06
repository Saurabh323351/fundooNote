"""
models.py

    This is responsible to create tables in the database.

        Actually here in this models.py ,we create blueprint of tables
        According blueprint ,tables will be created inside database


Author: Saurabh Singh

Since : 4 Feb , 2019
"""

from django.db import models
from django.contrib.auth.models import User


# create profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # create image field
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
