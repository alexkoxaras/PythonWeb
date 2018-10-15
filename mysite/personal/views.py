from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TopicForm, GameForm
from django.views.generic import CreateView

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

def gamedb(request):
	return render(request, 'personal/gamedb.html')
	
def post_new(request):
	if request.method == "POST":
		form = GameForm(request.POST or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
	else:
		form = GameForm()
	return render(request, 'personal/gamedb.html', {'form': form})