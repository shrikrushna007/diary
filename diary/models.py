from django.db import models
from django.utils import timezone

class Entry(models.Model):
    header = models.CharField(max_length=255)
    entry = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
