from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name='users'

urlpatterns = [
    path('register',views.register,name='register'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('alamat',views.tambahalamat,name='tambah-alamat'),
    path('alamat/edit',views.editalamat,name='edit-alamat'),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]