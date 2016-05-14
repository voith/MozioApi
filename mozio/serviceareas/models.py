from __future__ import unicode_literals

from django.contrib.gis.db import models
# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=2)  # ISO 639-1
    currency = models.CharField(max_length=3)  # ISO 4217

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    poly = models.PolygonField()
    provider = models.ForeignKey('Provider')

    def __str__(self):
        return self.name
