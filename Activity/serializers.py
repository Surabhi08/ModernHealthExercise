
from rest_framework import serializers
from .models import *

#serializer for activity table
class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = ['name', 'description', 'text']
