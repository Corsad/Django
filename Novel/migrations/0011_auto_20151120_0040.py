# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Novel', '0010_remove_vol_title2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(unique=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='novel',
            name='slug',
            field=models.SlugField(unique=True, max_length=300),
        ),
    ]
