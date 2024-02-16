from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from gearmasterapi.models import Gear

class GearView(ViewSet):
  def list(self, request):
    """Getting all gear"""
    gear = Gear.objects.all()
    serializer = GearSerializer(gear, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk):
    """Getting single gear"""
    try:
      gear = Gear.objects.get(pk=pk)
    except Gear.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GearSerializer(gear)
    return Response(serializer.data)
  
  def create(self, request):
    """Creating a new gear"""
    gear = Gear.objects.create(
      name=request.data['name'],
      info=request.data['info'])
    
    gear.save()
    serializer = GearSerializer(gear)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Updating a gear"""
    gear = Gear.objects.get(pk=pk)
    gear.name = request.data['name']
    gear.info = request.data['info']
    
    gear.save()
    serializer = GearSerializer(gear)
    return Response(serializer.data)

class GearSerializer(serializers.ModelSerializer):
  """serializer for gear"""
  class Meta:
    model = Gear
    fields = ('id', 'name', 'info')
    depth = 1
