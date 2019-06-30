# Create your models here.
from django.db import models
from datetime import datetime
from companies.models import Company


class Contact(models.Model):
  company =  models.ForeignKey(Company, on_delete=models.DO_NOTHING)
  name = models.CharField(max_length=200)
  person_id = models.IntegerField()
  c_name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name