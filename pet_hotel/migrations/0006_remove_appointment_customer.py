# Generated by Django 4.0 on 2022-12-01 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_hotel', '0005_alter_appointment_customer_alter_appointment_pet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='customer',
        ),
    ]
