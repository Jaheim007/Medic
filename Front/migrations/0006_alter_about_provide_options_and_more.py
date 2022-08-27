# Generated by Django 4.1 on 2022-08-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0005_alter_about_us_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_provide',
            options={'verbose_name': 'About_provide', 'verbose_name_plural': 'About_provide'},
        ),
        migrations.AlterModelOptions(
            name='about_stats',
            options={'verbose_name': 'About_Stats', 'verbose_name_plural': 'About_Stats'},
        ),
        migrations.AlterModelOptions(
            name='about_us',
            options={'verbose_name': 'About_Us', 'verbose_name_plural': 'About_Us'},
        ),
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Appointment', 'verbose_name_plural': 'Appointment'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'Banner'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='departments',
            options={'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='doctors',
            options={'verbose_name': 'Doctor', 'verbose_name_plural': 'Doctors'},
        ),
        migrations.AlterModelOptions(
            name='emergency_banner',
            options={'verbose_name': 'Emergency_banner', 'verbose_name_plural': 'Emergency_banner'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Newsletter', 'verbose_name_plural': 'Newsletters'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Services', 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='services_banner',
            options={'verbose_name': 'Services_banner', 'verbose_name_plural': 'Services_banner'},
        ),
        migrations.AlterModelOptions(
            name='siteinfo',
            options={'verbose_name': 'SiteInfo', 'verbose_name_plural': 'SiteInfo'},
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AddField(
            model_name='departments',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
