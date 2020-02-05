from django.shortcuts import render
from testimoni.models import testi
from produk.models import barang
from blog.models import artikel
from slider.models import gambar

def index(request):
    data_testi = testi.objects.all().order_by('-id')[0:4]
    data_barang = barang.objects.all().filter(status_aktiv=1).order_by('-id')[0:8]
    data_artikel = artikel.objects.all().order_by('-id')[0:3]
    data_slider = gambar.objects.all().order_by('-id')[0:3]
    
    #parsing data
    context = {
        'testi':data_testi,
        'produk':data_barang,
        'artikel':data_artikel,
        'slider':data_slider,
    }
    return render(request,'index.html',context)
