# Generated by Django 3.2 on 2022-01-19 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservations',
            new_name='Reservation',
        ),
        migrations.RenameModel(
            old_name='Tables',
            new_name='Table',
        ),
    ]
