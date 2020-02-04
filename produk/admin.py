from django.contrib import admin
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class kategoriResource(resources.ModelResource):

	class Meta:
		model = models.kategori
		fields = ('nama','tanggal_buat',)
        
class barangResource(resources.ModelResource):

	class Meta:
		model = models.barang
		fields = ('nama','deskripsi','harga','diskon','tanggal_buat','kategori','status_aktiv',)

class roleskategori(ImportExportModelAdmin):
    resource_class = kategoriResource
    list_display = ('nama','tanggal_buat')
    list_filter = ('tanggal_buat',)
    readonly_fields = ('tanggal_buat','slug')
    icon_name='bookmark'

admin.site.register(models.kategori,roleskategori)

class rolesbarang(ImportExportModelAdmin):
    resource_class = barangResource
    list_display = ('nama', 'harga', 'diskon','kategori','tanggal_buat','status_aktiv',)
    list_filter = ('kategori','tanggal_buat')
    readonly_fields = ('tanggal_buat','slug')
    icon_name='next_week'

    def status_aktiv(self, obj):
        return obj.benevolence_factor > 75

    status_aktiv.boolean = True

admin.site.register(models.barang,rolesbarang)
