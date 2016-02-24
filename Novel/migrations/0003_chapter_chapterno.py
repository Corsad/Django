# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Novel', '0002_auto_20151111_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapterNo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
