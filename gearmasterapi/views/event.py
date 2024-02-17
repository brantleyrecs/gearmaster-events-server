from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from rest_framework.decorators import action
from gearmasterapi.models import User, Type, Event, EventGear, Gear

class EventNiew(ViewSet):
  def list(self, request):
    """Getting all events"""
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk):
    """Gets single event"""
    event = Event.objects.get(pk=pk)
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Create event"""
    user_id = User.objects.get(pk=request.data["userId"])
    type_id = Type.objects.get(pk=request.data["typeId"])
    
    event = Event.objects.create(
      user=user_id,
      type=type_id,
      name=request.data["name"],
      date=request.data["date"],
      time=request.data["time"],
      location=request.data["location"],
      )
    
    event.save()
    serializer = EventSerializer(event)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Update event"""
    event = Event.objects.get(pk=pk)
    event.name=request.data["name"]
    event.date=request.data["date"]
    event.time=request.data["time"]
    event.location=request.data["location"]
    
    user_id=User.objects.get(pk=request.data["userId"])
    event.user=user_id
    
    type_id=Type.objects.get(pk=request.data["typeId"])
    event.type=type_id
    
    event.save()
    serializer = EventSerializer(event)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Delete event"""
    event = Event.objects.get(pk=pk)
    event.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  @action(methods=['post'], detail=True)
  def event_gear(self, request, pk):
    """Method to post a single piece of gear to an event"""
    event_id = Event.objects.get(pk=pk)
    gear_id = Gear.objects.get(pk=request.data["gear"])
    event_gear = EventGear.objects.create(
      gear=gear_id,
      event=event_id,
      )
    return Response(status=status.HTTP_201_CREATED)
  
class EventGearSerializer(serializers.ModelSerializer):
  name = serializers.ReadOnlyField(source='gear.name')
  info = serializers.ReadOnlyField(source='gear.info')
  
  class Meta:
    model = EventGear
    fields = ('id', 'name', 'info')
    

class EventSerializer(serializers.ModelSerializer):
  """serializer for event"""
  gear = EventGearSerializer(many=True, read_only=True)
  class Meta:
    model = Event
    fields = ('id', 'name', 'location', 'date', 'time', 'user', 'type', 'event_gear')
