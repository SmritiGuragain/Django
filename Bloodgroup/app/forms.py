from django import forms
from .models import doner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class addform(forms.ModelForm):
    class Meta:
        model=doner
        fields='__all__'


class userform(UserCreationForm):
    model=User
    fields=['Username','Email','password1','password2']
