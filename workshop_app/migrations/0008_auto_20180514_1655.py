# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-14 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop_app', '0007_auto_20180510_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('computer engineering', 'Computer Science'), ('information technology', 'Information Technology'), ('civil engineering', 'Civil Engineering'), ('electrical engineering', 'Electrical Engineering'), ('mechanical engineering', 'Mechanical Engineering'), ('chemical engineering', 'Chemical Engineering'), ('aerospace engineering', 'Aerospace Engineering'), ('biosciences and bioengineering', 'Biosciences and  BioEngineering'), ('electronics', 'Electronics'), ('energy science and engineering', 'Energy Science and Engineering')], max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='how_did_you_hear_about_us',
            field=models.CharField(blank=True, choices=[('FOSSEE website', 'FOSSEE website'), ('Google', 'Google'), ('Social Media', 'Social Media'), ('From other College', 'From other College')], max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, choices=[('Professor', 'Prof.'), ('Doctor', 'Dr.'), ('Shriman', 'Shri'), ('Shrimati', 'Smt'), ('Kumari', 'Ku'), ('Mr', 'Mr.'), ('Mrs', 'Mrs.'), ('Miss', 'Ms.')], max_length=32),
        ),
    ]
