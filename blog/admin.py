from django.contrib import admin
from . import models

# Register your models here.
class rolekategori(admin.ModelAdmin):
    list_display = ('nama',)
    readonly_fields = ['tanggal','slug']
    list_filter = ('tanggal',)
    icon_name='bookmark'

admin.site.register(models.kategori,rolekategori)

class roleartikel(admin.ModelAdmin):
    list_display = ('judul','isi','gambar','kategori',)
    readonly_fields = ['tanggal','slug']
    list_filter = ('tanggal','kategori',)
    icon_name = 'art_track'

admin.site.register(models.artikel,roleartikel)

admin.site.site_header = "Toko Lancar Jaya"

