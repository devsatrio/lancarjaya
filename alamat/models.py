from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class pengguna(models.Model):
    pengguna = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    label = models.CharField(max_length=100)
    kota = models.CharField(max_length=100)
    kode_kota = models.CharField(max_length=100)
    alamat_lengkap = models.TextField()

    def __str__(self):
        return self.label

