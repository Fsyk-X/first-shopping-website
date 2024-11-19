# Generated by Django 5.1.1 on 2024-09-17 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_custaddress_order_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='custAddress',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='custCity',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='custEmail',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='custName',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='custState',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='zipcode',
            new_name='custZipcode',
        ),
    ]