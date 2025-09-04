from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def jadwal(request):
    return render(request, 'jadwal.html')

def live(request):
    return render(request, 'live.html')

def saran(request):
    return render(request, 'saran.html')
