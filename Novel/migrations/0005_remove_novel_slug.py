# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Novel', '0004_auto_20151119_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novel',
            name='slug',
        ),
    ]
