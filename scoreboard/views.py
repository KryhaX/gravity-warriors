from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def scoreboard(request):
    return render(request, 'scoreboard.html')
