from django.db import models
from django.utils.text import slugify

class contact(models.Model):
	nomer_hp_satu = models.CharField(max_length=20)
	nomer_hp_dua = models.CharField(max_length=20)
	deskripsi = models.TextField()
	alamat = models.TextField()
	email = models.EmailField()
	instagram = models.CharField(max_length=100)
	facebook = models.CharField(max_length=100)
	moto = models.CharField(max_length=100)
	kota = models.CharField(max_length=100)
	kode_kota = models.CharField(max_length=100)
	
	def __str__(self):
		return self.moto
