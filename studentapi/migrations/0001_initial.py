# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('collegename', models.CharField(max_length=40)),
                ('age', models.CharField(max_length=40)),
                ('regnum', models.CharField(max_length=40)),
                ('dob', models.CharField(max_length=40)),
                ('university', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
