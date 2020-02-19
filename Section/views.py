from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
import json
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from Activity.models import Activity
from Activity.serializers import ActivitySerializer
from .models import Section 
from .serializers import SectionSerializer
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class SectionViewSet(mixins.RetrieveModelMixin, GenericViewSet):
		queryset = Section.objects.all()
		serializer_class = SectionSerializer

		#retreive method will be called on GET request for section with  arguments
		def retrieve(self, request, *args, **kwargs):
			try:
				section_details = Section.objects.filter(program = kwargs['program_id'], id = kwargs['section_id'])[0]
				serializer = SectionSerializer(instance = section_details)
				return Response(serializer.data)
			except:
				raise APIException('No section found with program id ' + str(kwargs['program_id']) + ", section id " + str(kwargs['section_id']))
			