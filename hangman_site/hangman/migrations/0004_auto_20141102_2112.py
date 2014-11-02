# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0003_auto_20141102_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='guessed_words',
            new_name='guessed_letters',
        ),
        migrations.AddField(
            model_name='game',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
