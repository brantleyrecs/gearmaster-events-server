from django.db import models
from .event import Event
from .gear import Gear

class EventGear(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='gear')
  gear = models.ForeignKey(Gear, on_delete=models.CASCADE, related_name='gear')
