# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_storefront', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField(default=1)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon_storefront.ProductTypes')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangazon_storefront.Customer')),
            ],
        ),
    ]