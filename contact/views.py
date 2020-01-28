from django.shortcuts import render
from . import models

def index(request):
	data_kontak = models.contact.objects.all().order_by('id')[0:3]

	#parsing data
	context = {
		'contact':data_kontak
	}
	return render(request, 'contact/index.html',context)
