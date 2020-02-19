from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.core import serializers
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class ActivityViewSet(mixins.RetrieveModelMixin, GenericViewSet):
		queryset = Activity.objects.all()
		serializer_class = ActivitySerializer

		#retrieve method will be called on a GET request with the arguments in kwargs
		def retrieve(self, request, *args, **kwargs):
			try:
				activity_details = Activity.objects.filter(program = kwargs['program_id'], section = kwargs['section_id'], id = kwargs['activity_id'])[0]
				serializer = ActivitySerializer(instance = activity_details)
				
				# to check if the data is html or mcq, if the data is mcq, get the questions and a list of choices
				if serializer.data['description'] == 2:
					question, mcq = serializer.data['text'].split('?')
					choices = mcq.split(',')
				else:
					html = serializer.data['text']
				
				return Response(serializer.data)
			except:
				raise APIException(" No activity found with program id " + str(kwargs['program_id']) + ", section id " + str(kwargs['section_id'])\
					+ " activity id " + str(kwargs['activity_id']))
				