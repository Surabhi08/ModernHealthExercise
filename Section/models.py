from django.db import models
from ProgramLibrary.models import Program

#model to create Section table with fields and program as the foreign key from Program model
class Section(models.Model):
	name = models.TextField()
	description = models.TextField()
	image = models.ImageField(upload_to = 'images/')
	order_index = models.IntegerField()
	program = models.ForeignKey(Program, on_delete = models.CASCADE, related_name = 'section_program')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('order_index',)
