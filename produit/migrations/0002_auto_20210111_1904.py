# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-11 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.ManyToManyField(to='produit.Tag'),
        ),
    ]
