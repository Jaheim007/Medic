# Generated by Django 4.1 on 2022-08-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0002_alter_appointment_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
