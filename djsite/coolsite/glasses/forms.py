from django import forms
from .models import *


class AddUser(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'