from django.db import models

#code to create Program table with name and description as the fields
class Program(models.Model):
	name = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)
