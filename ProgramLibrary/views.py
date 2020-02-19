from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.core import serializers
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .models import Program
from .serializers import ProgramSerializer
from Section.models import Section
from rest_framework.response import Response


class ProgramViewSet(mixins.RetrieveModelMixin,GenericViewSet):
		queryset = Program.objects.all()
		serializer_class = ProgramSerializer
		
		#retrieve method will be called when a get request is made with the parameters passed
		def retrieve(self, request, pk = None):
			prog = Program.objects.filter(id = pk)[0]
			serialize = ProgramSerializer(instance = prog)
			return Response(serialize.data)
			
			
			
			
