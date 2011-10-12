from django.db import models
from django.db.models.signals import pre_save

from scup.utils.models import TimestampAbstract


class Tournament(TimestampAbstract):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to="tournaments/images")
  date = models.DateField()
  location = models.CharField(max_length=255, help_text="Enter an address that can be located using Google Maps. Leave blank to manually enter lat and lon.", default='', blank=True)
  lat = models.FloatField(default=0)
  lon = models.FloatField(default=0)
  
  class Meta:
    pass
  
  def __unicode__(self):
    year = self.year()
    return "%s (%s)"%(self.name,year)
  
  def year(self):
    return self.date.year
  
  # assuming that we're never having a competition at the equator and prime meridian
  def has_location(self):
    if self.lat is not 0 and self.lon is not 0:
      return True
    return False
    


def add_geolocation(sender, instance, using, **kwargs):
  import json, urllib, urllib2
  
  if instance.location != '':
    loc_encoded = urllib.quote_plus(instance.location)
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % loc_encoded
    result = json.load(urllib2.urlopen(url, None, 5))

    if result['status'] == 'OK' and result['results'][0]['geometry'].__contains__('location'):
      instance.lat = result['results'][0]['geometry']['location']['lat']
      instance.lon = result['results'][0]['geometry']['location']['lng']      
    
pre_save.connect(add_geolocation, sender=Tournament)