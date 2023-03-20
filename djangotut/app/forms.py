from django import forms
from app.models import donerModel

class addForm(forms.ModelForm):
    class Meta:
        model=donerModel
        fields='__all__'