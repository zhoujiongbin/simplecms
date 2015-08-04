# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('cat_id', models.AutoField(serialize=False, primary_key=True)),
                ('cat_name', models.CharField(max_length=100)),
                ('cat_father', models.IntegerField()),
            ],
        ),
    ]
