from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gearmasterapi.models import Event, Gear, EventGear

class EventGearView(ViewSet):
    def retrieve(self, request, pk):
        """GET Single event gear"""
        event_gear = EventGear.objects.get(pk=pk)
        serializer = EventGearSerializer(event_gear)
        return Response(serializer.data)
      
    def list(self, request):
      """GET All event gear"""
      event_gear = EventGear.objects.all()
      serializer = EventGearSerializer(event_gear, many=True)
      return Response(serializer.data)
    
    def destroy(self, request, pk):
        """Handles Delete request for an event gear"""
        
        eventGear = EventGear.objects.get(pk=pk)
        eventGear.delete()
        return Response(None)
    

class EventGearSerializer(serializers.ModelSerializer):
    """JSON serializer for event gear"""
    class Meta:
        model = EventGear
        fields = ('id', 'event', 'gear')
        depth = 1
