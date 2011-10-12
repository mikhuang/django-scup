from django.db import models

from scup.utils.models import TimestampAbstract

class Material(TimestampAbstract):
  year = models.IntegerField()
  name = models.CharField(max_length=255)
  file = models.FileField(upload_to="materials")
  cover = models.ImageField(upload_to="materials/covers")
  
  class Meta:
    pass
    
  def __unicode__(self):
    return "%s (%d)"%(self.name,self.year)