from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from produk.models import barang

class keranjang(models.Model):
    pembeli = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    barang = models.ForeignKey(barang,on_delete=models.SET_NULL,null=True)
    jumlah = models.IntegerField()
    berat_total = models.IntegerField(default=0)
    total = models.IntegerField(null=True,default=0)
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    kode_transaksi = models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.barang.nama

class transaksi(models.Model):
    kode_transaksi = models.CharField(max_length=150,null=True)
    pembeli = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    subtotal = models.IntegerField(default=0)
    ongkir = models.IntegerField(default=0)
    berat_total = models.IntegerField(default=0)
    total_biaya = models.IntegerField(null=True,default=0)
    tanggal_beli = models.DateTimeField(auto_now_add=True)
    opsi_pengiriman = models.CharField(max_length=150,null=True)
    status_verifikasi = models.BooleanField(default=False)
    tanggal_verivikasi = models.DateTimeField(null=True)
    resi_pengiriman = models.CharField(max_length=150,null=True,blank=True)
    
    def __str__(self):
        return self.opsi_pengiriman
