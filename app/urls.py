from django.urls import path
from . import views

urlpatterns = [
    path('jadwal/', views.jadwal_list, name='jadwal_list'),
    path('jadwal/create/', views.jadwal_create, name='jadwal_create'),
    path('jadwal/update/<int:pk>/', views.jadwal_update, name='jadwal_update'),
    path('jadwal/delete/<int:pk>/', views.jadwal_delete, name='jadwal_delete'),
    path("live/", views.live_tvri, name="live_tvri"),
]

