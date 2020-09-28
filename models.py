from django.db import models

# Create your models here.

class Video(models.Model):
	ResolutionHigh =  models.FileField(upload_to='static/videos/high', null=True)
	ResolutionMedium = models.FileField(upload_to='static/videos/medium', null=True)
	ResolutionLow = models.FileField(upload_to='static/videos/low', null=True)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
