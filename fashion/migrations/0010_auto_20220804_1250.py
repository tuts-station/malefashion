# Generated by Django 3.2.6 on 2022-08-04 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0009_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2022, 8, 4)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
