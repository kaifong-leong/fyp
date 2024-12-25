from django.db import models
from django.utils import timezone

class URLItem(models.Model):
    url = models.CharField(max_length=200, verbose_name="URL")
    date = models.DateTimeField(default=timezone.now)
    value_sslv2 = models.CharField(max_length=100, default="Unknown")
    value_sslv3 = models.CharField(max_length=100, default="Unknown")
    value_tls1 = models.CharField(max_length=100, default="Unknown")
    value_tls11 = models.CharField(max_length=100, default="Unknown")
    value_tls12 = models.CharField(max_length=100, default="Unknown")
    value_tls13 = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.url
    
class Policy(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
class PolicyRule(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
class Rule(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
class Subrule(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name