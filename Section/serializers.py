from rest_framework import serializers
from .models import *
from Activity.serializers import ActivitySerializer

#serializer for Section table with nested activity serializer to fetch acitivities for the particular section
class SectionSerializer(serializers.ModelSerializer):
	activity_section = ActivitySerializer(many = True, read_only = True)

	class Meta:
		model = Section
		fields = ['name', 'description', 'image', 'order_index', 'activity_section']