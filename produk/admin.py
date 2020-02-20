from django.contrib import admin
from django.shortcuts import redirect
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.urls import path

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
    list_per_page = 8
    date_hierarchy = 'tanggal_buat'
    # change_list_template = "produk/link_download.html"

    def status_aktiv(self, obj):
        return obj.benevolence_factor > 75
    status_aktiv.boolean = True
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('downloadfile/', self.downloadfile),
        ]
        return my_urls + urls

    def downloadfile(self, request):
        self.message_user(request, "Your csv file has been imported")
        return redirect("..")
        
admin.site.register(models.barang,rolesbarang)
