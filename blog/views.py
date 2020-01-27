from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

def index(request):
    data_kategori = models.kategori.objects.all()
    data_artikel = models.artikel.objects.all().order_by('-id')
    paginator = Paginator(data_artikel, 4)
    page = request.GET.get('page')
    data_artikel = paginator.get_page(page)

    #parsing data
    context = {
        'kategori':data_kategori,
        'artikel':data_artikel,
    }
    return render(request, 'blog/index.html',context)

def show(request,blogslug):
    detail_artikel = models.artikel.objects.get(slug=blogslug)
    artikel_lain = models.artikel.objects.all().order_by('?')[0:3]

    #parsing data
    context = {
        'detail_artikel':detail_artikel,
        'artikel_lain':artikel_lain,
    }
    return render(request,'blog/show.html',context)

def bykategori(request,kategori):
    data_kategori = models.kategori.objects.all()
    data_artikel = models.artikel.objects.all().filter(kategori=kategori).order_by('-id')
    paginator = Paginator(data_artikel, 4)
    page = request.GET.get('page')
    data_artikel = paginator.get_page(page)
    detail_kategori = models.kategori.objects.get(id=kategori)

    #parsing data
    context = {
        'detail_kategori':detail_kategori,
        'kategori':data_kategori,
        'artikel':data_artikel,
    }
    return render(request,'blog/kategori.html',context)




