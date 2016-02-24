# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Novel', '0009_vol_title2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vol',
            name='title2',
        ),
    ]
