from django.urls import path
from . import views

app_name='galeri'

urlpatterns = [
	# path('kategori/<int:kategori>',views.index,name='kategori'),
	path('',views.index,name='index'),
]
