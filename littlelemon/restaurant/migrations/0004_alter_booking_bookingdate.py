# Generated by Django 4.2.5 on 2023-09-11 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 11, 7, 33, 54, 456428)),
        ),
    ]