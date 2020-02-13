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
		fields = ('nama','deskripsi','harga','diskon','tanggal_buat','berat','stok','kategori','status_aktiv',)

class roleskategori(ImportExportModelAdmin):
    resource_class = kategoriResource
    list_display = ('nama','tanggal_buat')
    list_filter = ('tanggal_buat',)
    readonly_fields = ('tanggal_buat','slug')
    icon_name='bookmark'

admin.site.register(models.kategori,roleskategori)

def aktivkan_produk(modeladmin, request, queryset):
    queryset.update(status_aktiv=1)
aktivkan_produk.short_description = "Aktivkan Produk"

def nonaktivkan_produk(modeladmin, request, queryset):
    queryset.update(status_aktiv=0)
nonaktivkan_produk.short_description = "Non Aktivkan Produk"

class rolesbarang(ImportExportModelAdmin):
    resource_class = barangResource
    list_display = ('nama', 'harga', 'stok','diskon','kategori','tanggal_buat','status_aktiv',)
    list_filter = ('kategori','tanggal_buat','status_aktiv')
    readonly_fields = ('tanggal_buat','slug')
    actions = [aktivkan_produk,nonaktivkan_produk]
    icon_name='next_week'

    def status_aktiv(self, obj):
        return obj.benevolence_factor > 75

    status_aktiv.boolean = True

admin.site.register(models.barang,rolesbarang)
