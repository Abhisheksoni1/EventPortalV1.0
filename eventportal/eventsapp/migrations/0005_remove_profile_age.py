# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0004_auto_20170824_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
    ]
