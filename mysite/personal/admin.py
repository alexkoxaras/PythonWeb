from django.contrib import admin
from .models import Game, Topic

# Register your models here.

class GameAdmin(admin.ModelAdmin):
	list_display = ('game_title', 'game_subtitle')
	search_fields = ('game_subjects', 'game_title')
	#filter_horizontal = ('game_title',)
	
class TopicAdmin(admin.ModelAdmin):
	list_display = ('topic_entry', 'topic_anotherfield')
	search_fields = ('topic_entry', 'topic_anotherfield',)

admin.site.register(Game, GameAdmin)
admin.site.register(Topic, TopicAdmin)
