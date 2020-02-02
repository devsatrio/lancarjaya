from django.db import models

class gambar(models.Model):
    head = models.CharField(max_length=35)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='slider/',null=True)

    def __str__(self):
        return self.head

