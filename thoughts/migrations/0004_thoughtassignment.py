# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20141227_2021'),
        ('thoughts', '0003_auto_20141127_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThoughtAssignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payments', models.ManyToManyField(to='payments.Payment')),
                ('thought', models.ForeignKey(to='thoughts.Thought', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
