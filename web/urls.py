from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
     path('admin/', admin.site.urls),
     path('', include('app.urls')),
    path('jadwal/', views.jadwal, name='jadwal'),
    path('live/', views.live, name='live'),
    path('saran/', views.saran, name='saran'),
]

