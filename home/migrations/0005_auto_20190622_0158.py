# Generated by Django 2.0.7 on 2019-06-21 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190622_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacy',
            name='title',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='terms',
            name='title',
            field=models.CharField(default='', max_length=15),
        ),
    ]
