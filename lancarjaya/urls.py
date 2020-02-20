from django.contrib import admin
from django.conf import settings	
from django.urls import path , include
from django.conf.urls.static import static
from . import views
admin.site.site_header = "Lancar Jaya Shop"
admin.site.site_title = "LJS"
admin.site.index_title = "Lancar Jaya Shop Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('produk/',include('produk.urls')),
    path('galeri/',include('galeri.urls')),
    path('testimoni/',include('testimoni.urls')),
    path('kontak/',include('contact.urls')),
    path('cara_belanja/',views.cara_belanja,name='cara_belanja'),
    path('cara_verifikasi/',views.cara_verifikasi,name='cara_verifikasi'),
    path('user/',include('users.urls')),
    path('pencarian/',views.pencarian,name='pencarian'),
    path('keranjang/',include('transaksi.urls')),
    path('',views.index,name='index'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

