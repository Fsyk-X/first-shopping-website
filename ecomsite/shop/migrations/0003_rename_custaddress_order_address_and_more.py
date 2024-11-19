# Generated by Django 5.1.1 on 2024-09-17 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custAddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='custCity',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='custEmail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='custName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='custState',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='custZipcode',
            new_name='zipcode',
        ),
    ]
