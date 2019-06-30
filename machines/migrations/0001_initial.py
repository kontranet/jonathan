# Generated by Django 2.2.1 on 2019-05-14 17:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=50)),
                ('licence_no', models.CharField(max_length=50)),
                ('licence_expiry', models.DateField()),
                ('operator_name', models.CharField(max_length=50)),
                ('op_mobile', models.CharField(max_length=30)),
                ('op_nextofkin', models.CharField(max_length=50)),
                ('op_nextofkin_mobile', models.CharField(max_length=30)),
                ('op_bloodtype', models.CharField(max_length=50)),
                ('comment', models.TextField(max_length=500)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('op_photo', models.ImageField(blank='True', upload_to='photos/machine_operators/%Y/%m/%d')),
                ('m_photo', models.ImageField(blank='True', upload_to='photos/machines/%Y/%m/%d')),
                ('licence_photo_1', models.ImageField(blank='True', upload_to='photos/machines_l/%Y/%m/%d')),
                ('licence_photo_2', models.ImageField(blank='True', upload_to='photos/machines_l/%Y/%m/%d')),
                ('licence_photo_3', models.ImageField(blank='True', upload_to='photos/machines_l/%Y/%m/%d')),
                ('licence_photo_4', models.ImageField(blank='True', upload_to='photos/machines_l/%Y/%m/%d')),
                ('licence_photo_5', models.ImageField(blank='True', upload_to='photos/machines_l/%Y/%m/%d')),
                ('machine_qrcode', models.FileField(blank='True', upload_to='m_qrcodes/%Y/%m/%d')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Company')),
            ],
        ),
    ]
