from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

def index(request):
	data_kategori = models.kategori.objects.all()
	data_galeri = models.foto.objects.all().order_by('-id')
	paginator = Paginator(data_galeri, 9)
	page = request.GET.get('page')
	data_galeri = paginator.get_page(page)

	#parsing data
	context = {
		'kategori':data_kategori,
		'galeri':data_galeri,
	}
	return render(request, 'galeri/index.html',context)

