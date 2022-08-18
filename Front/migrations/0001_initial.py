# Generated by Django 4.1 on 2022-08-18 12:31

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


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
            name='About_provide',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=150)),
            ],
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='About_Stats',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('number_stats', models.IntegerField()),
                ('icon', models.CharField(max_length=150)),
            ],
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('department', models.CharField(max_length=150)),
                ('appointment_date', models.DateField(auto_now_add=True)),
                ('doctor', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
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
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('name', models.CharField(max_length=150)),
                ('occupation', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='Doctor__Images')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Emergency_banner',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=150)),
            ],
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Services_banner',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=150)),
            ],
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
            bases=('Front.repeatfields',),
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Front.repeatfields')),
                ('name', models.CharField(max_length=150)),
                ('occupation', models.CharField(max_length=150)),
                ('comment', models.TextField()),
            ],
            bases=('Front.repeatfields',),
        ),
    ]