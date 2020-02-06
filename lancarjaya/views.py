from django.shortcuts import render
from django.db.models import Q
from testimoni.models import testi
from produk.models import barang
from blog.models import artikel
from slider.models import gambar

def index(request):
    data_testi = testi.objects.all().order_by('-id')[0:4]
    data_barang = barang.objects.all().filter(status_aktiv=1).order_by('-id')[0:8]
    data_artikel = artikel.objects.all().filter(status_aktif=1).order_by('-id')[0:3]
    data_slider = gambar.objects.all().order_by('-id')[0:3]
    
    #parsing data
    context = {
        'testi':data_testi,
        'produk':data_barang,
        'artikel':data_artikel,
        'slider':data_slider,
    }
    return render(request,'index.html',context)

def pencarian(request):
    data = request.GET.get('cari')
    data_barang = barang.objects.filter(Q(nama__startswith=data)).filter(Q(status_aktiv=1)).order_by('-id')
    data_artikel = artikel.objects.filter(Q(judul__startswith=data)).order_by('-id')
    context = {
        'hasil':data_barang,
        'hasil2': data_artikel,
    }
    return render(request, 'pencarian.html',context)