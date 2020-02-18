from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from . import models
from contact import models as contactmodel
from django.core.paginator import Paginator
from transaksi.models import keranjang
from . import forms

def index(request):
    data_produk = models.barang.objects.all().filter(status_aktiv=1).order_by('-id')
    paginator = Paginator(data_produk, 9)
    page = request.GET.get('page')
    data_produk = paginator.get_page(page)
    data_kategori = models.kategori.objects.order_by('-id').all()
    context = {
        'produk':data_produk,
        'kategori':data_kategori,
    }
    return render(request,'produk/index.html',context)

def show(request,slugbarang):
    hargabarangnya = 0
    if request.method == 'POST':
        jumlahnya = keranjang.objects.filter(barang=models.barang.objects.get(id=request.POST['barang']),kode_transaksi__isnull=True,pembeli=User.objects.get(id=request.POST['user'])).count()
        dbarang = models.barang.objects.get(id=request.POST['barang'])
        if dbarang.diskon > 0:
            jumlahdiskon = int(dbarang.harga)*int(dbarang.diskon)/100
            hargabarangnya = (int(dbarang.harga)-int(jumlahdiskon))*int(request.POST['jumlah'])
        else:
            hargabarangnya = int(dbarang.harga)*int(request.POST['jumlah'])

        beratbarang = int(dbarang.berat)*int(request.POST['jumlah'])
        if jumlahnya > 0 :
            t = keranjang.objects.get(kode_transaksi__isnull=True,barang=models.barang.objects.get(id=request.POST['barang']), pembeli=User.objects.get(id=request.POST['user']))
            t.jumlah = int(t.jumlah) + int(request.POST['jumlah']) 
            t.total = int(t.total)+int(hargabarangnya)
            t.berat_total = int(t.berat_total) + int(beratbarang)
            t.save()
        else:
            keranjang.objects.create(
            jumlah=request.POST['jumlah'],
            barang = models.barang.objects.get(id=request.POST['barang']),
            pembeli = User.objects.get(id=request.POST['user']),
            berat_total = int(beratbarang),
            total= int(hargabarangnya),
            )
        
        messages.success(request,'Berhasil menambah ke keranjang belanja')
        return redirect('produk:show',slugbarang=slugbarang)

    data_kontak = contactmodel.contact.objects.all().order_by('-id')[0:1]
    data_barang = models.barang.objects.get(slug=slugbarang)
    context = {
        'barang':data_barang,
        'contact':data_kontak,
        'form':forms.form_keranjang,
    }
    return render(request,'produk/show.html',context)

def kategori(request,slugkategori):
    data_kategori = models.kategori.objects.get(slug=slugkategori)
    data_barang = models.barang.objects.filter(status_aktiv=1).filter(kategori=data_kategori.id).order_by('-id')
    data_list_kategori = models.kategori.objects.order_by('-id').all()
    context = {
        'produk':data_barang,
        'detailkategori':data_kategori,
        'kategori':data_list_kategori,
    }
    return render(request,'produk/kategori.html',context)
