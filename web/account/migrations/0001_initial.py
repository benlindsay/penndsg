# Generated by Django 2.0 on 2018-02-11 04:13

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('program', models.CharField(max_length=100, null=True)),
                ('grad_year', models.IntegerField(null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to=account.models.user_directory_path)),
                ('viewable', models.BooleanField(default=False)),
                ('degrees', models.ManyToManyField(to='account.Degree')),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbrev', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='schools',
            field=models.ManyToManyField(to='account.School'),
        ),
    ]
