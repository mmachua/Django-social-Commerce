# Generated by Django 2.0.7 on 2019-07-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20190703_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(max_length=1500, null=True),
        ),
    ]