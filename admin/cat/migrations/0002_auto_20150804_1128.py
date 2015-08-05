# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_id',
            field=models.AutoField(primary_key=True, auto_created=True, serialize=False),
        ),
    ]
