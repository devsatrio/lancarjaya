from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import testimoniform
from .models import testi
def index(request):
    if request.method == 'POST':
        testi.objects.create(
            nama=request.POST['nama'],
            email = request.POST['email'],
            perihal = request.POST['perihal'],
            deskripsi = request.POST['deskripsi'],
        )
        messages.success(request,'Makasih Atas Penilaianya')
        return redirect('testimoni:index')
    
    data_testi = testi.objects.all().order_by('-id')
    context = {
        'testimoniform':testimoniform(),
        'testi':data_testi,
    }
    return render(request,'testimoni/index.html',context)
