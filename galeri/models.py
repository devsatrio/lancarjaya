from django.db import models
from django.utils.text import slugify

class kategori(models.Model):
	nama = models.CharField(max_length=50,unique=True)
	tanggal_buat = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(editable=False,blank=True,null=True)

	def save(self):
		self.slug = slugify(self.nama)
		super(kategori, self).save()

	def __str__(self):
		return self.nama
	
class foto(models.Model):
	judul = models.CharField(max_length=50)
	deskripsi = models.TextField(max_length=300)
	gambar = models.ImageField(upload_to='foto/',null=True)
	tanggal = models.DateTimeField(auto_now_add=True,null=True)
	slug = models.SlugField(editable=False,blank=True,null=True)
	kategori = models.ForeignKey(kategori,on_delete=models.SET_NULL,null=True) 

	def save(self):
		self.slug = slugify(self.judul)
		super(foto, self).save()
			
	def __str__(self):
		return self.judul