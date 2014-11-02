# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0005_auto_20141102_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(default=b'Guess a word', max_length=50),
            preserve_default=True,
        ),
    ]
