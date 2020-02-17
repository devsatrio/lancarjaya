from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import keranjang
from produk.models import barang
from django.db.models import Sum
from django.contrib.auth.models import User



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
        hargabarangnya = 0
        data = request.get(id=request.POST['kode'])
        dbarang = models.barang.objects.get(id=request.POST['barang'])

        if dbarang.diskon > 0:
            jumlahdiskon = int(dbarang.harga)*int(dbarang.diskon)/100
            hargabarangnya = (int(dbarang.harga)-int(jumlahdiskon))*int(request.POST['jumlah'])
        else:
            hargabarangnya = int(dbarang.harga)*int(request.POST['jumlah'])

        if data > 0 :
            hargabarangnya = int(dbarang.harga)*int(request.POST['jumlah'])
            t.jumlah = int(request.POST['jumlah']) 
            t.total = int(t.total)+int(hargabarangnya)
            t.save()
        else:
            keranjang.objects.update(
            jumlah=request.POST['jumlah'],
            barang = models.barang.objects.get(id=request.POST['barang']),
            pembeli = User.objects.get(id=request.POST['user']),
            total= int(hargabarangnya),
            )
        messages.success(request,'Berhasil edit data')
        return redirect('transaksi:edit',kodeuser=kodeuser)