from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from produk.models import barang

class keranjang(models.Model):
    pembeli = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    barang = models.ForeignKey(barang,on_delete=models.SET_NULL,null=True)
    jumlah = models.IntegerField()
    tanggal_buat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.barang.nama
