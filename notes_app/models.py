from django.db import models
from datetime import datetime

class Note(models.Model):
	title = models.CharField(max_length = 40)
	content = models.CharField(max_length = 10000)
	time = models.CharField(max_length = 10)
	size = models.IntegerField(default = 1)

	def __str__(self):
		return self.title
		