# Generated by Django 2.2.10 on 2021-06-22 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='id',
            new_name='order_id',
        ),
    ]
