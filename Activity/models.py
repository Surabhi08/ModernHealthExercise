from django.db import models
from ProgramLibrary.models import Program
from Section.models import Section

#code to create Activity model with program and section as foreign key 
class Activity(models.Model):
	# 1 is HTML and 2 is MCQ
	name = models.CharField(max_length = 50)
	text = models.TextField()
	description = models.IntegerField(default = 0)
	program = models.ForeignKey(Program, on_delete = models.CASCADE, related_name = 'activity_program')
	section = models.ForeignKey(Section, on_delete = models.CASCADE, related_name = 'activity_section')

	def __str__(self):
		return self.name


