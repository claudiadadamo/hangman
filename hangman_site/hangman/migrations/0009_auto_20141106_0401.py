# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0008_auto_20141106_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(default=b'New Game - Guess a letter', max_length=50),
            preserve_default=True,
        ),
    ]
