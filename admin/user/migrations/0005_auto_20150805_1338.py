# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20150805_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
