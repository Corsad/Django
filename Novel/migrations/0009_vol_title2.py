# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Novel', '0008_chapter_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='vol',
            name='title2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
