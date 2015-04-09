# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_text',
            field=models.CharField(default=datetime.datetime(2015, 4, 8, 18, 2, 57, 381773), max_length=500),
            preserve_default=False,
        ),
    ]
