# Generated by Django 5.1.1 on 2024-09-17 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
