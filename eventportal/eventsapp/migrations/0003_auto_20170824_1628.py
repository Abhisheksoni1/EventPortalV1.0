# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventsapp', '0002_auto_20170824_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sex', models.CharField(default=b'male', max_length=10, choices=[(b'male', b'MALE'), (b'female', b'FEMALE'), (b'other', b'OTHER')])),
                ('age', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-created',)},
        ),
    ]
