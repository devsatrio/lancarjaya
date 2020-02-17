from django.urls import path
from . import views
app_name = 'transaksi'
urlpatterns = [
    path('<str:kodeuser>',views.listkeranjang,name='keranjang'),
    path('editkeranjang/<str:kodeuser>',views.edit,name='edit'),
    path('hapuskeranjang/<str:kodeuser>',views.hapuskeranjang,name='hapus-keranjang'),
]