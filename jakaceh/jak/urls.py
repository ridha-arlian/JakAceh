from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required
from .views import UpdateUserView

urlpatterns = [
    path('', views.index, name='index'),
    path('registrasi/', views.registrasi, name='registrasi'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('angkutan/', views.angkutan, name='angkutan'),
    path('kuliner/', views.kuliner, name='kuliner'),
    path('penginapan/', views.penginapan, name='penginapan'),
    path('souvenir/', views.souvenir, name='souvenir'),
    path('wisata/', views.wisata, name='wisata'),
    path('informasi/rumah-sakit/', views.rumahsakit, name='rumah-sakit'),
    path('informasi/bengkel/', views.bengkel, name='bengkel'),
    path('informasi/polisi/', views.polisi, name='polisi'),
    path('informasi/minimarket/', views.minimarket, name='minimarket'),
    path('informasi/spbu/', views.spbu, name='spbu'),
    path('profil/', views.profil, name='profil'),
    path('logout', views.logout, name='logout'),
    path('update/', views.UpdateUserView.as_view(), name='update'),
]
