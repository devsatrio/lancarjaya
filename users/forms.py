from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from alamat.models import pengguna

class Userregisterform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-md input-md form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(label='Nama Depan',widget=forms.TextInput(attrs={'class': 'input-md form-control', 'placeholder': 'First Name'}), max_length=32)
    last_name=forms.CharField(label='Nama Belakang',widget=forms.TextInput(attrs={'class': 'input-md form-control', 'placeholder': 'Last Name'}), max_length=32)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-md form-control', 'placeholder': 'Email'}), max_length=64)
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'input-md form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(label='Konfirmasi Password',widget=forms.PasswordInput(attrs={'class': 'input-md form-control', 'placeholder': 'Password Again'}))


    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class Userchangedform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-md input-md form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(label='Nama Depan',widget=forms.TextInput(attrs={'class': 'input-md form-control', 'placeholder': 'First Name'}), max_length=32)
    last_name=forms.CharField(label='Nama Belakang',widget=forms.TextInput(attrs={'class': 'input-md form-control', 'placeholder': 'Last Name'}), max_length=32)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-md form-control', 'placeholder': 'Email'}), max_length=64)
    

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class alamatuser(forms.Form):
    label = forms.CharField(widget=forms.TextInput(attrs={'class':'input-md input-md form-control','placeholder':'Label Alamat'}))
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    kota = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class':'input-md input-md form-control','placeholder':'Label Alamat'}))
    Alamat_lengkap = forms.CharField(widget=forms.Textarea(attrs={'class':'input-md input-md form-control','placeholder':'Label Alamat'}))
            