# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=20, default='超级管理员')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.BinaryField()),
                ('account', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('joined_time', models.DateTimeField(default=datetime.datetime.now)),
                ('last_login', models.TimeField(null=True)),
                ('power', models.ForeignKey(to='user.Power', default=1)),
            ],
        ),
    ]
