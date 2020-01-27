from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

def index(request):
    data_produk = models.barang.objects.all().order_by('-id')
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
    data_barang = models.barang.objects.get(slug=slugbarang)
    context = {
        'barang':data_barang,
    }
    return render(request,'produk/show.html',context)

def kategori(request,slugkategori):
    data_kategori = models.kategori.objects.get(slug=slugkategori)
    data_barang = models.barang.objects.filter(kategori=data_kategori.id).order_by('-id')
    data_list_kategori = models.kategori.objects.order_by('-id').all()
    context = {
        'produk':data_barang,
        'detailkategori':data_kategori,
        'kategori':data_list_kategori,
    }
    return render(request,'produk/kategori.html',context)
