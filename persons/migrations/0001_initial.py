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
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dateofbirth', models.DateField()),
                ('mobile', models.CharField(max_length=30)),
                ('nextofkin', models.CharField(max_length=50)),
                ('nextofkin_mobile', models.CharField(max_length=30)),
                ('bloodtype', models.CharField(max_length=50)),
                ('comment', models.TextField(max_length=500)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank='True', upload_to='photos/pesrons/%Y/%m/%d')),
                ('licence_photo_1', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_2', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_3', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_4', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_5', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_6', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_7', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_8', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_9', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_10', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_11', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_13', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_14', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('licence_photo_12', models.ImageField(blank='True', upload_to='photos/persons_l/%Y/%m/%d')),
                ('person_qrcode', models.FileField(blank='True', upload_to='p_qrcodes/%Y/%m/%d')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Company')),
            ],
        ),
    ]
