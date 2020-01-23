from django.db import models

class kategori(models.Model):
    nama = models.CharField(max_length=50)
    tanggal_buat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class barang(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    diskon = models.IntegerField()
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    kategori = models.ForeignKey(kategori,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.nama