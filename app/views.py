from django.shortcuts import render, redirect, get_object_or_404
from .models import Jadwal
from .forms import JadwalForm
import requests
from .forms import JadwalFormSet

def jadwal_list(request):
    jadwals = Jadwal.objects.all()
    return render(request, 'jadwal_list.html', {'jadwals': jadwals})

def jadwal_create(request):
    if request.method == "POST":
        formset = JadwalFormSet(request.POST, queryset=Jadwal.objects.none())
        if formset.is_valid():
            formset.save()
            return redirect("jadwal_list")
    else:
        formset = JadwalFormSet(queryset=Jadwal.objects.none())

    return render(request, "jadwal_form.html", {"formset": formset})

def jadwal_update(request):
    if request.method == "POST":
        formset = JadwalFormSet(request.POST, queryset=Jadwal.objects.all())
        if formset.is_valid():
            formset.save()
            return redirect("jadwal_list")
    else:
        formset = JadwalFormSet(queryset=Jadwal.objects.all())

    return render(request, "jadwal_form.html", {"formset": formset})
def jadwal_delete(request, pk):
    jadwal = get_object_or_404(Jadwal, pk=pk)
    if request.method == 'POST':
        jadwal.delete()
        return redirect('jadwal_list')
    return render(request, 'jadwal_delete.html', {'jadwal': jadwal})

API_KEY = "AIzaSyCOyxduxxMam_gLAfxPfYL2HdgUi3SW90g"
CHANNEL_ID = "UCjtIzhP7MMzl3ZODYnRrJkw"  
YT_URL = "https://www.googleapis.com/youtube/v3/search"

def live_tvri(request):
    params = {
        "part": "snippet",
        "channelId": CHANNEL_ID,
        "eventType": "live",
        "type": "video",
        "key": API_KEY
    }
    res = requests.get(YT_URL, params=params).json()
    video_id = None
    if res.get("items"):
        video_id = res["items"][0]["id"]["videoId"]

    return render(request, "live.html", {"video_id": video_id})
