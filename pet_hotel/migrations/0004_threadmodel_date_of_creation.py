# Generated by Django 4.0 on 2022-12-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_hotel', '0003_threadmodel_messagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadmodel',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, default='2022-07-20 12:00:00'),
            preserve_default=False,
        ),
    ]
