# Generated by Django 3.2.16 on 2023-03-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeapp', '0002_auto_20230303_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='cc',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bike',
            name='price',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
