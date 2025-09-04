from django.db import models

class Jadwal(models.Model):
    nama_acara = models.CharField(max_length=200)
    tanggal = models.DateField(blank=True, null=True)
    waktu = models.TimeField(blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nama_acara} ({self.tanggal})"
