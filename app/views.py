from django.shortcuts import render, redirect, get_object_or_404
from .models import Jadwal
from .forms import JadwalForm
import requests

def jadwal_list(request):
    jadwals = Jadwal.objects.all()
    return render(request, 'jadwal_list.html', {'jadwals': jadwals})

def jadwal_create(request):
    if request.method == 'POST':
        form = JadwalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jadwal_list')
    else:
        form = JadwalForm()
    return render(request, 'jadwal_form.html', {'form': form})

def jadwal_update(request, pk):
    jadwal = get_object_or_404(Jadwal, pk=pk)
    if request.method == 'POST':
        form = JadwalForm(request.POST, instance=jadwal)
        if form.is_valid():
            form.save()
            return redirect('jadwal_list')
    else:
        form = JadwalForm(instance=jadwal)
    return render(request, 'jadwal_form.html', {'form': form})

def jadwal_delete(request, pk):
    jadwal = get_object_or_404(Jadwal, pk=pk)
    if request.method == 'POST':
        jadwal.delete()
        return redirect('jadwal_list')
    return render(request, 'jadwal_confirm_delete.html', {'jadwal': jadwal})

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
