from django.contrib import admin
from .models import pengguna

class rolespengguna(admin.ModelAdmin):
    list_display = ('label','pengguna','kota','alamat_lengkap',)
    list_filter = ('kota',)

admin.site.register(pengguna,rolespengguna)
