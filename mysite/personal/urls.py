from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^settings/', views.properties, name='properties'),
    url('^intro/', views.videointro, name='videointro'),
    url('^gameover/', views.gameended, name='gameended'),
    url('^game/', views.thegame, name='thegame'),
	url('^gamedb/', views.gamedb, name='gamedb')
]
