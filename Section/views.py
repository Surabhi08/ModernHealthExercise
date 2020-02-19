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

class SectionViewSet(mixins.RetrieveModelMixin, GenericViewSet):
		queryset = Section.objects.all()
		serializer_class = SectionSerializer

		#retreive method will be called on GET request for section with  arguments
		def retrieve(self, request, *args, **kwargs):
			
			section_details = Section.objects.filter(id = kwargs['section_id'])[0]
			serializer = SectionSerializer(instance = section_details)
			return Response(serializer.data)
			