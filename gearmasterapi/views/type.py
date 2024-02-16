from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from gearmasterapi.models import Type

class TypeView(ViewSet):
  def list(self, request):
    """Getting all types"""
    types = Type.objects.all()
    serializer = TypeSerializer(types, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk):
    """Getting single type"""
    try:
      type = Type.objects.get(pk=pk)
    except Type.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TypeSerializer(type)
    return Response(serializer.data)
  
  def create(self, request):
    """Creating a new type"""
    type = Type.objects.create(
      name=request.data['name'])
    
    type.save()
    serializer = TypeSerializer(type)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Updating a type"""
    type = Type.objects.get(pk=pk)
    type.name = request.data['name']
    
    type.save()
    serializer = TypeSerializer(type)
    return Response(serializer.data)

class TypeSerializer(serializers.ModelSerializer):
  """serializer for type"""
  class Meta:
    model = Type
    fields = ('id', 'name')
    depth = 1