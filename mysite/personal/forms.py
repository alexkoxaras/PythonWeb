from django import forms

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields= ["game_title", "game_link"]