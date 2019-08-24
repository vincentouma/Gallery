# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-24 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.CharField(max_length=30)),
                ('image', models.ImageField(default='', upload_to='gallery/')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pics.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pics.Place')),
            ],
        ),
    ]
