from django.contrib import admin
from django.conf import settings
from django.contrib.auth import get_user_model
from . import models

class rolestransaksi(admin.ModelAdmin):
    list_display = ('pembeli','barang','tanggal_buat','berat_total','jumlah','total')

admin.site.register(models.keranjang,rolestransaksi)

class rolestransaksis(admin.ModelAdmin):
    list_display = ('pembeli','tanggal_beli','opsi_pengiriman')

admin.site.register(models.transaksi,rolestransaksis)
