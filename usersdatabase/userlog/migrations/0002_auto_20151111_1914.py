# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweeter',
            name='userid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
