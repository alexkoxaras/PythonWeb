from django.db import models


class Topic (models.Model):
	topic_entry = models.CharField(max_length=30, verbose_name ='Μεθοδολογία')
	topic_anotherfield = models.DateField(auto_now_add=True, verbose_name ='Ημερομηνία')
	
	class Meta:
		ordering = ['topic_entry']
		verbose_name = "Ενότητα"
		verbose_name_plural = "Ενότητες"
	
	def __str__ (self):
		return(self.topic_entry)
	
	
class Game(models.Model):
	game_title = models.CharField(max_length=60, blank=True, verbose_name ='Τίτλος')
	game_subtitle = models.CharField(max_length=50, blank=True, verbose_name ='Υπότιτλος')
	game_image = models.FileField(upload_to='images/', null=True, blank=True,verbose_name ='Εικόνα')
	game_link = models.FileField(upload_to='docs/', null=True, blank=True,verbose_name ='Οδηγίες')
	game_dateimported = models.DateTimeField(auto_now_add=True, editable=False, verbose_name ='Ημερομηνία Ένταξης')
	game_subjects = models.ManyToManyField(Topic, verbose_name ='Θεματολογια')
	#game_subjects = models.ForeignKey('Topic', verbose_name ='Θεματολογια 1', on_delete=models.CASCADE)
	game_minpersons = models.IntegerField(blank=True, verbose_name ='Ελάχιστος αρ. ατόμων')
	game_maxpersons = models.IntegerField(blank=True, verbose_name ='Μέγιστος αρ. ατόμων')
	game_minteams = models.IntegerField(blank=True, verbose_name ='Ελάχιστος αρ. ομάδων')
	game_maxteams = models.IntegerField(blank=True, verbose_name ='Μέγιστος αρ. ομάδων')
	game_minfacilitators = models.IntegerField(blank=True, verbose_name ='Αριθμός ελάχιστων Facilitators')
	game_timeneeded = models.CharField(max_length=30, blank=True, verbose_name ='Ελάχιστος χρόνος')
	game_environment = models.CharField(max_length=50, blank=True, verbose_name ='Τόπος εκπαίδευσης')
	game_materials = models.CharField(max_length=100, blank=True, verbose_name ='Υλικά που απαιτούνται')
	game_portable = models.CharField(max_length=30, blank=True, verbose_name ='Φορητότητα')
	
	class Meta:
		ordering = ['game_title']
		verbose_name = "Παιχνίδι"
		verbose_name_plural = "Παιχνίδια"
	
	def __str__ (self):
		return u'%s %s' % (self.game_title, self.game_subtitle)