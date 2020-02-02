from django.contrib import admin
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# class ProdukResource(resources.ModelResource):

# 	class Meta:
# 		model = models.kategori
# 		fields = ('id','nama','tanggal_buat')

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
