from django.urls import path
from . import views
app_name='testimoni'

urlpatterns = [
    path('',views.index,name='index'),
    
]