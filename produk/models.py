from django.db import models
from django.utils.text import slugify

class kategori(models.Model):
    nama = models.CharField(max_length=50,unique=True)
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,editable=False)
    
    def save(self):
      self.slug=slugify(self.nama)
      super(kategori, self).save()

    def __str__(self):
        return self.nama

class barang(models.Model):
    nama = models.CharField(max_length=50,unique=True)
    deskripsi = models.TextField()
    harga = models.IntegerField()
    diskon = models.IntegerField()
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    kategori = models.ForeignKey(kategori,on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(null=True,editable=False)
    
    def save(self):
      self.slug=slugify(self.nama)
      super(barang, self).save()

    def __str__(self):
        return self.nama