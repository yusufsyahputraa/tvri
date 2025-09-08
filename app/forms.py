from django import forms
from .models import Jadwal
from django.forms import modelformset_factory

class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = ["acara", "tanggal", "waktu_mulai", "waktu_selesai"]
        widgets = {
            "tanggal": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "waktu_mulai": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "waktu_selesai": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "acara": forms.Select(attrs={"class": "form-control"}),
        }

JadwalFormSet = modelformset_factory(
    Jadwal,
    fields=("acara", "tanggal", "waktu_mulai", "waktu_selesai"),
    extra=5 ,
    can_delete=True,
)