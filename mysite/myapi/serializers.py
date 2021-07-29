from rest_framework import serializers

from .models import Hero,Comedians

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class ComediansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comedians
        fields = ('name', 'alias')

