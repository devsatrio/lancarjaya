from django.shortcuts import render

def index(request):
    context = {
        'title':'halo',
    }
    return render(request,'index.html',context)