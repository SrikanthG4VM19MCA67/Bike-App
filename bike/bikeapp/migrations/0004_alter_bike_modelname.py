# Generated by Django 4.1.7 on 2023-03-08 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeapp', '0003_auto_20230303_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='modelname',
            field=models.CharField(max_length=20),
        ),
    ]