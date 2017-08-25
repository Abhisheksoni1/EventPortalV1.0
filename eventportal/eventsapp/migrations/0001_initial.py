# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date=b'created')),
                ('venue', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000, blank=True)),
                ('event_time', models.DateTimeField()),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
