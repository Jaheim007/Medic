# Generated by Django 4.1 on 2022-09-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default=' default.jpg ', upload_to='User__Images'),
        ),
    ]