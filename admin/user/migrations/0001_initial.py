# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.BinaryField()),
                ('account', models.CharField(unique=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('power', models.IntegerField()),
                ('joined_time', models.TimeField(default=datetime.datetime(2015, 8, 4, 16, 3, 59, 817609))),
                ('last_login', models.TimeField(null=True)),
            ],
        ),
    ]
