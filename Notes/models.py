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
from django.utils import timezone

# Create your models here.
from django.urls import reverse
from datetime import date


class Notes(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    reminder = models.DateTimeField(default=timezone.now)  # add kiya
    # date = models.DateField(default=date.today)##add kiya

    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    color = models.CharField(default=None, max_length=50, blank=True, null=True)
    image = models.ImageField(default=None, null=True)
    trash = models.BooleanField(default=False)
    is_pinned = models.BooleanField(blank=True, null=True, default=False)
    collaborate = models.ManyToManyField(User, blank=True, related_name='collaborated_user')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
