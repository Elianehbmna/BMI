# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-06 16:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='bio please...', max_length=100)),
                ('profilepic', models.ImageField(blank=True, default='../static/images/bad-profile-pic-2.jpeg', upload_to='profile/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(blank=True, default=0)),
                ('height', models.FloatField(blank=True, default=0)),
                ('BMI', models.FloatField(blank=True, default=0)),
                ('result', models.TextField(blank=True)),
                ('profiles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmiapp.Profile')),
            ],
        ),
    ]
