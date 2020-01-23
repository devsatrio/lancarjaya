from django.contrib import admin
from . import models
from import_export import resources

class tampil(admin.ModelAdmin):
	list_display=('nama','tanggal_buat')
	readonly_fields = ['tanggal_buat','slug']
	icon_name='bookmark'

admin.site.register(models.kategori,tampil)

class tampil_foto(admin.ModelAdmin):
	list_display=('judul','kategori','deskripsi','gambar','tanggal')
	readonly_fields = ['tanggal','slug']
	icon_name='wallpaper'

admin.site.register(models.foto,tampil_foto)
