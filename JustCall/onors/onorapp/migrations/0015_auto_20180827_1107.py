# Generated by Django 2.1 on 2018-08-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onorapp', '0014_auto_20180827_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registers',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
