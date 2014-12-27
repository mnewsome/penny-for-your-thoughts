# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_stripe_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='stripe_customer_id',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
