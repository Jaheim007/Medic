# Generated by Django 4.1 on 2022-08-18 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0004_remove_about_us_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_us',
            options={'ordering': ['title']},
        ),
    ]