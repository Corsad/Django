# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Novel', '0006_novel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='slug',
        ),
    ]
