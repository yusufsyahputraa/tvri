from django import forms
from .models import Jadwal

class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = ['nama_acara', 'tanggal', 'waktu', 'deskripsi']
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date'}),
            'waktu': forms.TimeInput(attrs={'type': 'time'}),
        }
