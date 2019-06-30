from django.db import models
from datetime import datetime
from companies.models import Company

class Person(models.Model):
    company =  models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    mobile = models.CharField(max_length=30)
    nextofkin = models.CharField(max_length=50)
    nextofkin_mobile = models.CharField(max_length=30)
    bloodtype = models.CharField(max_length=50)
    comment = models.TextField(max_length=500)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/pesrons/%Y/%m/%d', blank="True")
    licence_photo_1 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_2 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_3 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_4 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_5 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_6 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_7 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_8 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_9 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_10 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_11 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_12 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_13 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_14 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    licence_photo_12 = models.ImageField(upload_to='photos/persons_l/%Y/%m/%d', blank="True")
    person_qrcode = models.ImageField(upload_to='p_qrcodes/%Y/%m/%d', blank="True")
    def __str__(self):
        return self.name
        
