from django.contrib import admin
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class KategoriResource(resources.ModelResource):

	class Meta:
		model = models.kategori
		fields = ('nama','tanggal',)

class ArtikelResource(resources.ModelResource):

	class Meta:
		model = models.artikel
		fields = ('judul','isi','tanggal','kategori',)

class rolekategori(ImportExportModelAdmin):
	resource_class = KategoriResource
	list_display = ('nama','tanggal')
	readonly_fields = ['tanggal','slug']
	list_filter = ('tanggal',)
	icon_name='bookmark'

admin.site.register(models.kategori,rolekategori)


def aktifkan_produk(modeladmin, request, queryset):
    queryset.update(status_aktif=1)
aktifkan_produk.short_description = "Aktifkan Artikel"

def nonaktifkan_produk(modeladmin, request, queryset):
    queryset.update(status_aktif=0)
nonaktifkan_produk.short_description = "Non Aktifkan Artikel"


class roleartikel(ImportExportModelAdmin):
	resource_class = ArtikelResource
	list_display = ('judul','tanggal','gambar','kategori','status_aktif',)
	readonly_fields = ['tanggal','slug']
	list_filter = ('tanggal','kategori',)
	actions = [aktifkan_produk,nonaktifkan_produk]
	icon_name = 'art_track'

	def status_aktif(self, obj):
		return obj.benevolence_factor > 75

	status_aktif.boolean = True

admin.site.register(models.artikel,roleartikel)


