from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('redaksi', 'Redaksi'),
        ('viewer', 'Viewer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')

    def __str__(self):
        return f"{self.username} ({self.role})"

class Kategori(models.Model):
    nama = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nama

class Berita(models.Model):
    judul = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='berita/', blank=True, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)
    penulis = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

class Acara(models.Model):
    nama = models.CharField(max_length=200, unique=True)
    deskripsi = models.TextField(blank=True, null=True)
    kategori = models.CharField(
        max_length=100,
        choices=[
            ('Berita', 'Berita'),
            ('Hiburan', 'Hiburan'),
            ('Olahraga', 'Olahraga'),
            ('Anak', 'Anak'),
            ('Lainnya', 'Lainnya'),
        ],
        default='Lainnya'
    )

    def __str__(self):
        return self.nama

class Jadwal(models.Model):
    acara = models.CharField(max_length=200)
    tanggal = models.DateField()
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField(blank=True, null=True)
    editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.acara.nama} - {self.tanggal} {self.waktu_mulai}"

class Highlight(models.Model):
    berita = models.ForeignKey(Berita, on_delete=models.CASCADE)
    posisi = models.PositiveIntegerField(default=0)  # urutan tampil di slider

    def __str__(self):
        return f"Highlight: {self.berita.judul}"
