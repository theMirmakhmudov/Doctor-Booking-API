# Generated by Django 5.1.5 on 2025-01-27 08:10

import api.managers
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff')),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin'), ('manager', 'Manager'), ('doctor', 'Doctor')], default='user', max_length=10, verbose_name='role')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/', verbose_name='avatar')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', api.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=100, verbose_name='specialization')),
                ('experience', models.PositiveIntegerField(default=0, verbose_name='experience')),
                ('location', models.CharField(max_length=150, verbose_name='location')),
                ('clinic_name', models.CharField(max_length=150, verbose_name='clinic name')),
                ('consultation_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='consultation fee')),
                ('is_consultation_free', models.BooleanField(default=False, verbose_name='is_consultation_free')),
                ('availability_today', models.BooleanField(default=False, verbose_name='availability today')),
                ('rating_percentage', models.PositiveIntegerField(default=0, verbose_name='rating percentage')),
                ('patient_stories', models.PositiveIntegerField(default=0, verbose_name='patient stories')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctors',
            },
        ),
    ]
