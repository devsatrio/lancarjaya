from django.urls import path
from . import views

app_name='galeri'

urlpatterns = [
	path('',views.index,name='index'),
]
