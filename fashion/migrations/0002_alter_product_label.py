# Generated by Django 3.2.6 on 2022-07-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('New', 'New'), ('Best Seller', 'Best Seller'), ('Sale', 'Sale')], max_length=150),
        ),
    ]
