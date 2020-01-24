from django.db import models

class gambar(models.Model):
    nama = models.CharField(max_length=35)
    gambar = models.ImageField(upload_to='slider/',null=True)

    def __str__(self):
        return self.nama

