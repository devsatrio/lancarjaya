from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import keranjang
from produk.models import barang
from django.db.models import Avg
from django.contrib.auth.models import User

@login_required
def listkeranjang(request,kodeuser):
    data_keranjang = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser))
    subtotal = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser)).aggregate(Avg('barang'))
    context = {
        'barang':data_keranjang,
        'subtotal':subtotal,
    }
    return render(request,'transaksi/cart.html',context)

@login_required
def hapuskeranjang(request,kodeuser):
    if request.method == 'POST':
        data = keranjang.objects.get(id=request.POST['kode'])
        data.delete()
        messages.success(request,'Berhasil menghapus barang dari keranjang')
        return redirect('transaksi:keranjang',kodeuser=kodeuser)
    

    data_keranjang = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser))
    context = {
        'barang':data_keranjang,
    }
    return render(request,'transaksi/cart.html',context)