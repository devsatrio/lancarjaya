from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import http.client
from contact.models import contact
from .models import keranjang
from produk.models import barang
from django.db.models import Sum
from django.contrib.auth.models import User
from alamat.models import pengguna
import json


@login_required
def listkeranjang(request,kodeuser):
    jne = ''
    data_keranjang = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser))
    subtotal = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser)).aggregate(Sum('total'))
    totalbarang = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser)).aggregate(Sum('jumlah'))
    totalberat = keranjang.objects.filter(pembeli=User.objects.get(username=kodeuser)).aggregate(Sum('berat_total'))
    cekalamat = pengguna.objects.filter(pengguna=User.objects.get(username=kodeuser)).count()
    
    webdata = contact.objects.get(id=1)
    desti = pengguna.objects.get(pengguna=User.objects.get(username=kodeuser))
    conn = http.client.HTTPSConnection("api.rajaongkir.com")
    payload = "origin="+webdata.kode_kota+"&destination="+desti.kode_kota+"&weight="+str(totalberat['berat_total__sum'])+"&courier=jne"
    headers = {
        'key': "5c9d1c918e391d9fee83d59759943b59",
        'content-type': "application/x-www-form-urlencoded"
    }
    conn.request("POST", "/starter/cost", payload, headers)
    res = conn.getresponse()
    data = res.read()
    jne = json.loads(data)
    print(jne)
    context = {
        'barang':data_keranjang,
        'cekalamat':cekalamat,
        'jne':jne,
    }
    context.update(subtotal)
    context.update(totalbarang)
    context.update(totalberat)
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
    hargabarangnya = 0
    if request.method == 'POST':
        dbarang = barang.objects.get(id=request.POST['barang'])

        if dbarang.diskon > 0:
            jumlahdiskon = int(dbarang.harga)*int(dbarang.diskon)/100
            hargabarangnya = (int(dbarang.harga)-int(jumlahdiskon))*int(request.POST['jumlah'])
        else:
            hargabarangnya = int(dbarang.harga)*int(request.POST['jumlah'])
        
        beratbarang = int(dbarang.berat)*int(request.POST['jumlah'])
        t = keranjang.objects.get(id=request.POST['kode'])
        t.jumlah = request.POST['jumlah'] 
        t.total = hargabarangnya
        t.berat_total = beratbarang
        t.save()
        messages.success(request,'Berhasil edit data')
    return redirect('transaksi:keranjang',kodeuser=kodeuser)