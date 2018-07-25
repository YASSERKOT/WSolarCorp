from django.db import models
import os
import json
from copy import deepcopy

class User(models.Model):
    """This class represents the User model."""
    identifier = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    region = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} {} {} {}".format(self.identifier, self.name, self.email, self.region)

class Layer(models.Model):
    """This class represents the Layer model."""
    identifier = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    hight = models.DecimalField(max_digits=19, decimal_places=2)
    width = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} {} {} {}".format(self.identifier, self.name, self.high, self.width)

class Regions():
    """ this class represents the Region model which read from the files geoJson file """
    def getAllRegions():
        with open('custom.geo.json') as f:
            data = json.load(f)
        jsonData = json.dumps(data)
        return jsonData

    def getRegion(name):
        d = {'continent': {'name': '',
                        'subregion': '',
                        'country': {'name': '',
                                    'formal_en': '',
                                    'coordinates': {}
                                    }
                        }
        }
        lst = []
        with open('custom.geo.json') as f:
            data = json.load(f)
        for feature in data['features']:
            if feature['properties']['name'].upper() == name.upper() :
                d['continent']['name'] = feature['properties']['continent']
                d['continent']['subregion'] = feature['properties']['subregion']
                d['continent']['country']['name'] = feature['properties']['name']
                d['continent']['country']['formal_en'] = feature['properties']['formal_en']
                d['continent']['country']['coordinates'] = feature['geometry']['coordinates']
        jsonData = json.dumps(d)
        return jsonData