from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def properties(request):
	return render(request, 'personal/settings.html')

def videointro(request):
	return render(request, 'personal/intro.html')
