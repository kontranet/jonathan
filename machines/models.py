from django.db import models
from datetime import datetime
from companies.models import Company

class Machine(models.Model):
    company =  models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    machine_name = models.CharField(max_length=50)
    licence_no = models.CharField(max_length=50)
    licence_expiry = models.DateField()
    operator_name = models.CharField(max_length=50)
    op_mobile = models.CharField(max_length=30)
    op_nextofkin = models.CharField(max_length=50)
    op_nextofkin_mobile = models.CharField(max_length=30)
    op_bloodtype = models.CharField(max_length=50)
    comment = models.TextField(max_length=500)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    op_photo = models.ImageField(upload_to='photos/machine_operators/%Y/%m/%d', blank="True")
    m_photo = models.ImageField(upload_to='photos/machines/%Y/%m/%d', blank="True")
    licence_photo_1 = models.ImageField(upload_to='photos/machines_l/%Y/%m/%d', blank="True")
    licence_photo_2 = models.ImageField(upload_to='photos/machines_l/%Y/%m/%d', blank="True")
    licence_photo_3 = models.ImageField(upload_to='photos/machines_l/%Y/%m/%d', blank="True")
    licence_photo_4 = models.ImageField(upload_to='photos/machines_l/%Y/%m/%d', blank="True")
    licence_photo_5 = models.ImageField(upload_to='photos/machines_l/%Y/%m/%d', blank="True")
    machine_qrcode = models.FileField(upload_to='m_qrcodes/%Y/%m/%d', blank="True")
    def __str__(self):
        return self.machine_name
        
