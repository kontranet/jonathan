from django.db import models
from datetime import datetime

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='photos/company_logos/%Y/%m/%d', blank="True")
    company_qrcode = models.FileField(upload_to='company_qrcodes/%Y/%m/%d', blank="True")
    def __str__(self):
        return self.company_name
        