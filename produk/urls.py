from django.urls import path
from . import views
app_name = 'produk'

urlpatterns=[
    path('',views.index,name='index'),
    path('<slug:slugbarang>',views.show,name='show'),
    path('kategori/<slug:slugkategori>',views.kategori,name='kategori')
]