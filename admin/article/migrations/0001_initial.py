# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('article_title', models.CharField(max_length=200)),
                ('publish_time', models.DateTimeField(verbose_name='date published')),
                ('article_author', models.CharField(max_length=50)),
                ('article_content', models.TextField()),
                ('article_cat_id', models.ForeignKey(to='cat.Cat')),
            ],
        ),
    ]
