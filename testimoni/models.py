from django.db import models

class testi(models.Model):
    nama = models.CharField(max_length=80)
    email = models.EmailField()
    perihal = models.CharField(max_length=100)
    deskripsi = models.TextField()
    tanggal_buat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
