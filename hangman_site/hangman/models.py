from django.db import models

# Create your models here.
class Word(models.Model):
	word_text = models.CharField(max_length=10)
	word_length = models.IntegerField(default=0)