from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('kategori/<int:kategori>',views.bykategori,name='kategori'),
    path('<slug:blogslug>',views.show,name='show'),
    path('',views.index,name='index'),
]