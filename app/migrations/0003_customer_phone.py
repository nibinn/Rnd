# Generated by Django 2.2.10 on 2021-06-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210622_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]