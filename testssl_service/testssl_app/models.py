from django.db import models
from django.utils import timezone

class URLItem(models.Model):
    url = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.url