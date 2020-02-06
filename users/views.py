from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Userregisterform

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

def profile(request):
    context = {
        'head':'Profile User',
    }
    return render(request,'users/profile.html',context)


