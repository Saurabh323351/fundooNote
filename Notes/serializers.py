from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.Serializer):

    class Meta:
        model = Notes
        fields = '__all__'
