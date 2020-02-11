from django.contrib import admin
from django.conf import settings
from django.contrib.auth import get_user_model
from . import models

class rolestransaksi(admin.ModelAdmin):
    list_display = ('pembeli','barang','tanggal_buat','jumlah','total')

admin.site.register(models.keranjang,rolestransaksi)
