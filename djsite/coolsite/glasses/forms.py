from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddUser(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class OrderCreate(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('Customer_code', 'Payment_method', 'Delivery_date', 'Delivery_type', 'Delivery_adders',
                  'Delivery_price', 'Courier_code', 'Note')
