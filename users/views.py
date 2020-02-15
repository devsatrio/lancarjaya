from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from .forms import Userregisterform, Userchangedform

def register(request):
    if request.method == 'POST':
        form = Userregisterform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil Membuat akun')
            return redirect('users:register')
    else:
        form = Userregisterform()
    context = {
        'head':'Register User',
        'form':form,
    }
    return render(request,'users/register.html',context)

def editprofile(request):
    if request.method == 'POST':
        form = Userchangedform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil Memperbarui akun')
            return redirect('users:editprofile')
    else:
        form = Userchangedform(instance=request.user)

    context = {
        'form':form,
    }
    return render(request,'users/profile.html',context)


