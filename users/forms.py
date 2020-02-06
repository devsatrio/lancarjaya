from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Userregisterform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(label='Nama Depan',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32)
    last_name=forms.CharField(label='Nama Belakang',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64)
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(label='Konfirmasi Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))


    class Meta():
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        # fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)