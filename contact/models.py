from django.db import models
from django.utils.text import slugify

class contact(models.Model):
	nama = models.CharField(max_length=50,unique=True)
	nomer_hp = models.IntegerField()
	alamat = models.CharField(max_length=50,blank=True)
	email = models.EmailField(max_length=50,blank=True)
	tanggal_buat = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nama
