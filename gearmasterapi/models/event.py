from django.db import models
from .user import User
from .type import Type

class Event(models.Model):
  name = models.CharField(max_length=55)
  date = models.DateField()
  time = models.TimeField()
  location = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=0, related_name='user')
  type = models.ForeignKey(Type, on_delete=models.SET_DEFAULT, default=0, related_name='type')
