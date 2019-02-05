"""
serializers.py

    This is responsible to create serializer.


Author: Saurabh Singh

Since : 4 Feb , 2019
"""
from rest_framework import serializers
from .models import Notes


class NoteSerializer(serializers.Serializer):
    class Meta:
        model = Notes
        fields = '__all__'
