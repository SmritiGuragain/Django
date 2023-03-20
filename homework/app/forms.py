from django import forms
from .models import homework

class addform(forms.ModelForm):
    class Meta:
        model=homework
        fields='__all__'