"""ModernHealthExercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ProgramLibrary.views import ProgramViewSet
from Section.views import SectionViewSet 
from Activity.views import ActivityViewSet
from rest_framework.routers import DefaultRouter

api_router = DefaultRouter()
api_router.register(r'program', ProgramViewSet, 'program')
urlpatterns = api_router.urls
urlpatterns += [
    path('admin/', admin.site.urls),
    path('/', ProgramViewSet.as_view({'get':'list'}), name = 'program'),
    path('program/<int:program_id>/section/<int:section_id>/', SectionViewSet.as_view({'get':'retrieve'}), name = 'section'),
    path('program/<int:program_id>/section/<int:section_id>/activity/<int:activity_id>', ActivityViewSet.as_view({'get':'retrieve'}), name = 'activity'),

]