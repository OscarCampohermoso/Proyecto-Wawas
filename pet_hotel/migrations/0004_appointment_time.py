# Generated by Django 4.0 on 2022-11-30 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_hotel', '0003_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]