from django.db import models

class Note(models.Model):
	title = models.CharField(max_length = 40)
	content = models.CharField(max_length = 1000)

	def __str__(self):
		return self.title
		