# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ar', '0002_post_preview_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview_text',
            field=models.TextField(),
        ),
    ]
