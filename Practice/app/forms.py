from django import forms
from .models import info

class addform(forms.ModelForm):
    class Meta:
        model=info
        fields='__all__'