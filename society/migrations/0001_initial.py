# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0002_college_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=100)),
                ('icon', models.ImageField(max_length=200, upload_to=b'')),
                ('created_date', models.DateTimeField(verbose_name='created date')),
                ('department', models.CharField(max_length=100)),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.College')),
            ],
        ),
    ]