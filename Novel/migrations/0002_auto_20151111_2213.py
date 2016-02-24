# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Novel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='pub_dat',
            new_name='pub_date',
        ),
    ]
