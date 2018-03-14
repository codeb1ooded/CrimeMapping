from django.db import models

from django.contrib.auth.models import *

import datetime
# Create your models here.


class USER(models.Model):
  USER_REF = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="USER")
  NAME = models.CharField(max_length=100)
  PASSWORD= models.CharField(max_length=6)

  def __str__(self):
      return self.NAME

class FIR_REPORT(model.Model):
  CRIME_TYPE = models.CharField(max_length=100)
  LOCATION_LAT = models.IntegerField()
  LOCATION_LONG = models.IntegerField()
  CRIME_DES = models.CharField(max_length=1000)
  PERSON_COMPLAINT = models.ForeignKey(max_length=100)
  COMPLAINT_BY = models.CharField(max_length=100)
  DATE_CRIME = models.DateField(_(u"Conversation Date"), blank=True)
  TIME_CRIME = models.TimeField(_(u"Conversation Time"), blank=True)
  FIR_LOC = models.CharField(max_length=100)
  COMPLAINT_TIME = models.TimeField(_(u"Conversation Time"), blank=True)

  def __str__(self):
      return self.CRIME_TYPE
