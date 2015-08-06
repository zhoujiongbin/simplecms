# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150805_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('level', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=20, default='超级管理员')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='power',
            field=models.ForeignKey(to='user.Power'),
        ),
    ]
