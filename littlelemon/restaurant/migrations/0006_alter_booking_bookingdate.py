# Generated by Django 4.2.5 on 2023-09-12 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 6, 36, 32, 438964)),
        ),
    ]
