from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from gearmasterapi.models import User
from gearmasterapi.models import Type
from gearmasterapi.models import Event

class EventSerializer(serializers.ModelSerializer):
  """serializer for event"""
  class Meta:
    model = Event
    fields = ('id', 'name', 'location', 'date', 'time', 'user', 'type')