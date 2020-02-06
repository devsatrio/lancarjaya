from django.contrib import admin
from . import models

class tampil(admin.ModelAdmin):
	icon_name='build'

admin.site.register(models.contact,tampil)