from django.shortcuts import render
from django.db.models import Q
from produk.models import barang 
from django.core.paginator import Paginator

def index(request):
	# data_kategori = models.kategori.objects.all()
	data = request.GET.get('cari')
	data_barang = barang.objects.filter(Q(nama__startswith=data)).order_by('-id')
	# paginator = Paginator(data_galeri, 9)
	# page = request.GET.get('page')
	# data_galeri = paginator.get_page(page)

	#parsing data
	context = {
		'hasil':data_barang,
	}
	return render(request, 'cari/index.html',context)


