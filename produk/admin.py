from django.contrib import admin
from . import models

class roleskategori(admin.ModelAdmin):
    list_display = ('nama','tanggal_buat')
    list_filter = ('tanggal_buat',)
    readonly_fields = ('tanggal_buat','slug')
    icon_name='bookmark'

admin.site.register(models.kategori,roleskategori)

class rolesbarang(admin.ModelAdmin):
    list_display = ('nama', 'harga', 'diskon','kategori','tanggal_buat')
    list_filter = ('kategori','tanggal_buat')
    readonly_fields = ('tanggal_buat','slug')
    icon_name='next_week'

admin.site.register(models.barang,rolesbarang)
