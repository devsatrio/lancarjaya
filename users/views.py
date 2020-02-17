from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from .forms import Userregisterform, Userchangedform, alamatuser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from alamat.models import pengguna
import http.client
import json

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

@login_required
def tambahalamat(request):
    conn = http.client.HTTPSConnection("api.rajaongkir.com")
    
    if request.method == 'POST':
        newkota = request.POST['kota'].split('-')
        pengguna.objects.create(
            pengguna = User.objects.get(id=request.POST['kode']),
            label = request.POST['labelalamat'],
            alamat_lengkap = request.POST['alamat'],
            kota = newkota[1],
            kode_kota = newkota[0], 
        )
        messages.success(request, 'Berhasil Menambah Alamat')
        return redirect('users:editprofile')
    
    headers = { 'key': "5c9d1c918e391d9fee83d59759943b59" }
    conn.request("GET", "/starter/city", headers=headers)
    res = conn.getresponse()
    data = res.read()
    b = json.loads(data)
    form = alamatuser()
    context = {
        'form':form,
        'kota':b,
    }
    return render(request,'users/create_alamat.html',context)

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = Userchangedform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berhasil Memperbarui akun')
            return redirect('users:editprofile')
    else:
        form = Userchangedform(instance=request.user)
    
    data_alamat = '';
    jumlah_alamat = pengguna.objects.filter(pengguna=User.objects.get(id=request.user.id)).count()
    if jumlah_alamat > 0 :
        data_alamat = pengguna.objects.get(pengguna=User.objects.get(id=request.user.id))
    
    context = {
        'alamat':data_alamat,
        'form':form,
        'jumlah_alamat':jumlah_alamat,
    }
    return render(request,'users/profile.html',context)

@login_required
def editalamat(request):
    conn = http.client.HTTPSConnection("api.rajaongkir.com")
    
    if request.method == 'POST':
        newkota = request.POST['kota'].split('-')
        t = pengguna.objects.get(id=request.POST['kode'])
        t.label = request.POST['labelalamat'] 
        t.alamat_lengkap = request.POST['alamat']
        t.kota = newkota[1]
        t.kode_kota = newkota[0]
        t.save()
        messages.success(request, 'Berhasil Memperbarui Alamat')
        return redirect('users:editprofile')

    headers = { 'key': "5c9d1c918e391d9fee83d59759943b59" }
    conn.request("GET", "/starter/city", headers=headers)
    res = conn.getresponse()
    data = res.read()
    b = json.loads(data)
    form = alamatuser()
    
    data_alamat = pengguna.objects.get(pengguna=User.objects.get(id=request.user.id))
    context = {
        'form':form,
        'kota':b,
        'alamat':data_alamat,
    }
    return render(request,'users/edit_alamat.html',context)    