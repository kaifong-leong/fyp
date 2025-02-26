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
    tls10_ciphers = models.CharField(max_length=10000, default="Unknown")
    tls11_ciphers = models.CharField(max_length=10000, default="Unknown")
    tls12_ciphers = models.CharField(max_length=10000, default="Unknown")
    tls13_ciphers = models.CharField(max_length=10000, default="Unknown")
    kems = models.CharField(max_length=10000, default="Unknown")
    ecdhe_curves = models.CharField(max_length=10000, default="Unknown")
    tls12_sig_alg = models.CharField(max_length=10000, default="Unknown")
    tls13_sig_alg = models.CharField(max_length=10000, default="Unknown")
    cert_sig_alg = models.CharField(max_length=10000, default="Unknown")
    cert = models.CharField(max_length=10000, default="Unknown")

    def __str__(self):
        return self.url
    
"""
class TLSProtocolVersion(models.model): 
    major = models.IntegerField()
    minor = models.IntegerField()
    
class KEX():
    pass

class TestsslScan(models.Model):
    versions = models.ManyToManyField(
        TLSProtocolVersion,
        # to add values for TLSProtocolVersion, eg. offered/not offered
    )

    kexs = models.ManyToManyField(
        KEX,
        # to add values for KEX
    )

# Database will look like the following
TestsslScan_someNewId | version_someId | not_offered
TestsslScan_someNewId | version_someOtherId | offered  
"""

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