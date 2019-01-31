from django import forms
from .models import Notes

from django import forms
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.admin import widgets


class create_note_form(forms.ModelForm):
    class Meta:
        model = Notes
        widgets = {
          'description': forms.Textarea(attrs={'rows':1, 'cols':25})
        }
        fields = ('title', 'description', 'is_pinned', 'color')

class update_note_form(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Notes
        fields = ['id', 'title', 'description', 'is_pinned', 'color']

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class reminder_form(forms.ModelForm):
    reminder = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = Notes
        fields = ['reminder']


# class MyForm(Form):
#     my_field = DateField(widget=AdminDateWidget)

