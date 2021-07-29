from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer,ComediansSerializer
from .models import Hero,Comedians


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class ComediansViewSet(viewsets.ModelViewSet):
    queryset = Comedians.objects.all().order_by('name')
    serializer_class = ComediansSerializer

