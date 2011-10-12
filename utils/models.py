from django.db import models
from django.utils.translation import ugettext_lazy as _

class TimestampAbstract(models.Model):
  """
  Abstract base class that adds basic timestamps
  """
  date_created  = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract  = True

