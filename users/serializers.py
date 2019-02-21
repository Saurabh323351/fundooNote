"""
serializers.py

    This is responsible to create serializer.


Author: Saurabh Singh

Since : 4 Feb , 2019
"""

from rest_framework import serializers
from django.contrib.auth.models import User


class LoginCustomSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=200)
  password = serializers.CharField(max_length=200)


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('email', 'username',)
    read_only_fields = ( 'email', 'username' )
