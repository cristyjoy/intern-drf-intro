# Generated by Django 2.0.4 on 2018-05-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choj', '0002_auto_20180501_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
