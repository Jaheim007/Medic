# Generated by Django 4.1 on 2022-08-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0007_remove_about_stats_title_about_stats_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='description_2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about_us',
            name='list_item_1',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about_us',
            name='list_item_2',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about_us',
            name='list_item_3',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
