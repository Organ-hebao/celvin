# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='instance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('instanceName', models.CharField(max_length=50)),
                ('lanIp', models.GenericIPAddressField()),
                ('wanIpSet', models.GenericIPAddressField()),
                ('os', models.CharField(max_length=30)),
                ('zoneName', models.CharField(max_length=30)),
            ],
        ),
    ]