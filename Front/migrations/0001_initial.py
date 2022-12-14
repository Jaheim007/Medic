# Generated by Django 4.1 on 2022-08-30 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='RepeatFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='About_Stats',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('number_stats', models.IntegerField()),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'About_Stats',
                'verbose_name_plural': 'About_Stats',
            },
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('description_2', models.TextField()),
                ('list_item_1', models.CharField(max_length=150)),
                ('list_item_2', models.CharField(max_length=150)),
                ('list_item_3', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='About__Images')),
            ],
            options={
                'verbose_name': 'About_Us',
                'verbose_name_plural': 'About_Us',
            },
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='Banner__Images')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
            },
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Emergency_banner',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Emergency_banner',
                'verbose_name_plural': 'Emergency_banner',
            },
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletters',
            },
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('about_title', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('appointment_title', models.CharField(max_length=150)),
                ('contact_title', models.CharField(max_length=150)),
                ('copyright', models.CharField(max_length=150)),
                ('departments_title', models.CharField(max_length=150)),
                ('doctors_title', models.CharField(max_length=150)),
                ('opening_days', models.CharField(max_length=150)),
                ('services_title', models.CharField(max_length=150)),
                ('testimonials_title', models.CharField(max_length=150)),
                ('email_1', models.CharField(max_length=150)),
                ('email_2', models.CharField(max_length=150)),
                ('phone_1', models.CharField(max_length=150)),
                ('phone_2', models.CharField(max_length=150)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
            options={
                'verbose_name': 'SiteInfo',
                'verbose_name_plural': 'SiteInfo',
            },
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('name', models.CharField(max_length=150)),
                ('occupation', models.CharField(max_length=150)),
                ('comment', models.TextField()),
                ('image', models.ImageField(upload_to='Testimonial__Images')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
            bases=('Front.repeatfields',),
        ),
    ]
