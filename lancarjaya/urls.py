from django.contrib import admin
from django.conf import settings	
from django.urls import path , include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('produk/',include('produk.urls')),
    path('testimoni/',include('testimoni.urls')),
    path('kontak/',include('contact.urls')),
    path('',views.index,name='index'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

