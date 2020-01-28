from django.shortcuts import render
from .forms import testimoniform
def index(request):
    context = {
        'testimoniform':testimoniform(),
        'head':'halo',
    }
    return render(request,'testimoni/index.html',context)
