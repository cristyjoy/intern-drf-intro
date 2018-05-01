# Generated by Django 2.0.4 on 2018-05-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('picture', models.ImageField(upload_to='static/media')),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('date_createsd', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['director'],
            },
        ),
    ]
