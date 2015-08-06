# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150805_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='power',
            field=models.ForeignKey(default=1, to='user.Power'),
        ),
    ]
