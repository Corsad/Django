# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Novel', '0011_auto_20151120_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='slug',
            new_name='chapter_slug',
        ),
        migrations.RenameField(
            model_name='novel',
            old_name='slug',
            new_name='novel_slug',
        ),
    ]
