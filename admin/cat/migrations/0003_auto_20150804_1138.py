# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0002_auto_20150804_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
