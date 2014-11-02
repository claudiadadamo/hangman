# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0002_auto_20141102_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=100)),
                ('word_length', models.IntegerField(default=0)),
                ('current_state', models.CharField(max_length=100)),
                ('guessed_words', models.CharField(max_length=26)),
                ('wrong_guesses', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
