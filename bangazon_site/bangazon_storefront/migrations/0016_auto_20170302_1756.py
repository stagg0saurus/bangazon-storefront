# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_storefront', '0015_auto_20170302_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='bangazon_storefront.ProductTypes'),
        ),
    ]