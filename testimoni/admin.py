from django.contrib import admin
from . import models

class rolestesti(admin.ModelAdmin):
    list_display = ('nama','email','perihal','tanggal_buat')
    list_filter = ('tanggal_buat',)

admin.site.register(models.testi,rolestesti)
