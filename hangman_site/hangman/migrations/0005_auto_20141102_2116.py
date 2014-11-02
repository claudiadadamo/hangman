# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0004_auto_20141102_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='guessed_letters',
            field=models.CharField(default=b'', max_length=26),
            preserve_default=True,
        ),
    ]
