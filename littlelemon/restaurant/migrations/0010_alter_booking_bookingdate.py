# Generated by Django 4.2.5 on 2023-09-12 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_booking_bookingdate_alter_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 12, 6, 39, 0, 161048)),
        ),
    ]
