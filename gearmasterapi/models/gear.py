from django.db import models

class Gear(models.Model):
  name = models.CharField(max_length=55)
  info = models.CharField(max_length=200)
