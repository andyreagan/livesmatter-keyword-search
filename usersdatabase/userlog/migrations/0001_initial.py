# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweeter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted_date', models.DateTimeField(null=True, blank=True)),
                ('submitted', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=100, null=True, blank=True)),
                ('numtweetsfound', models.IntegerField(default=0)),
            ],
        ),
    ]
