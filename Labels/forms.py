from django import forms
from .models import Labels
class CreateLabels(forms.ModelForm):

    class Meta:
        model=Labels
        fields='__all__'
    # label=forms.CharField(max_length=100)

class UpdateLabels(forms.ModelForm):

    class Meta:
        model=Labels
        fields='__all__'
