from django.shortcuts import render
from testimoni.models import testi
from produk.models import barang
def index(request):
    data_testi = testi.objects.all().order_by('-id')[0:4]
    data_barang = barang.objects.all().order_by('-id')[0:8]
    context = {
        'testi':data_testi,
        'produk':data_barang,
    }
    return render(request,'index.html',context)