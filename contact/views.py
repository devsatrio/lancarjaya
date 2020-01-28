from django.shortcuts import render
from . import models

def index(request):
	data_kontak = models.contact.objects.all()

	#parsing data
	context = {
		'contact':data_kontak
	}
	return render(request, 'contact/index.html',context)
