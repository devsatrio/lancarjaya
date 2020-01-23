from django.contrib import admin
from . import models

class tampil(admin.ModelAdmin):
	list_display=('nama','nomer_hp','alamat','email','tanggal_buat')
	list_filter = ('tanggal_buat',)
	readonly_fields = ['tanggal_buat','slug']
	icon_name='build'

admin.site.register(models.contact,tampil)