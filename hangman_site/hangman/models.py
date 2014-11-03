from django.db import models

# Create your models here.
class Game(models.Model):
	word = models.CharField(max_length=100)
	word_length = models.IntegerField(default=0)
	current_state = models.CharField(max_length=100)
	guessed_letters = models.CharField(max_length=26,default='')
	wrong_guesses = models.IntegerField(default=0)
	current = models.BooleanField(default=False)
	status = models.CharField(max_length=50, default="Guess a word")

	def __str__(self):              # __unicode__ on Python 2
		return self.word

class Guess(models.Model):
	letter = models.CharField(max_length=1)

class Image(models.Model):
	name = models.CharField(max_length=10)

class Stats(models.Model):
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
