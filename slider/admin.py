from django.contrib import admin
from . import models

class rolegambar(admin.ModelAdmin):
    list_display = ('head','gambar',)
    list_filter = ('head',)
    icon_name = 'collections'

admin.site.register(models.gambar,rolegambar)

admin.site.site_header = "Toko Lancar Jaya"