from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'personal/home.html')

def properties(request):
	return render(request, 'personal/settings.html')

def videointro(request):
	return render(request, 'personal/intro.html')

def thegame(request):
	return render(request, 'personal/game.html')

def gameended(request):
	return render(request, 'personal/gameover.html')
