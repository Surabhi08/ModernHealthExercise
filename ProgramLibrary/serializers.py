from rest_framework import serializers
from .models import *
from Section.models import Section
from Section.serializers import SectionSerializer

#serializer for Program table with nested section serializer to fetch the sections for the particulare program
class ProgramSerializer(serializers.ModelSerializer):
	section_program = SectionSerializer(many = True, read_only = True)
	class Meta:
		model = Program
		fields = ['name', 'description', 'section_program']




