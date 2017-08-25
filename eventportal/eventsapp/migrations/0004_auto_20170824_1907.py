# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0003_auto_20170824_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_tickets', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='event_fee',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='event',
            field=models.ForeignKey(to='eventsapp.Event'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(to='eventsapp.Profile'),
        ),
    ]
