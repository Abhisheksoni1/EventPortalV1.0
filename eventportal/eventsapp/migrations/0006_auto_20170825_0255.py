# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0005_remove_profile_age'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together=set([('user', 'event')]),
        ),
    ]
