from django import forms
from .models import Topic
from .models import Game

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['topic_entry']
		
class GameForm(forms.ModelForm):
	class Meta:
		model = Game
		exclude = '__all__'