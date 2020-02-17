from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import keranjang
from produk.models import barang
from django.db.models import Sum
from django.contrib.auth.models import User
from .forms import Editform


@login_required
def listkeranjang(request,kodeuser):
    data_keranjang = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser))
    subtotal = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser)).aggregate(Sum('total'))
    totalbarang = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser)).aggregate(Sum('jumlah'))
    context = {
        'barang':data_keranjang,
    }
    context.update(subtotal)
    context.update(totalbarang)
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

@login_required
def edit(request,kodeuser):
    if request.method == 'POST':
        data = keranjang.objects.get(jumlah=request.POST['jumlah2'])
        data.update()
        messages.success(request,'Berhasil edit data')
        return redirect('transaksi:edit',kodeuser=kodeuser)