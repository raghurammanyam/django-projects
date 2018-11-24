# Generated by Django 2.1 on 2018-08-16 09:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onorapp', '0002_auto_20180813_0659'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carosuel',
            new_name='Carousel',
        ),
        migrations.RenameModel(
            old_name='CategoryCarosuel',
            new_name='CategoryCarousel',
        ),
        migrations.RenameModel(
            old_name='MainPageCarosuel',
            new_name='MainPageCarousel',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='carosuelname',
            new_name='carouselname',
        ),
        migrations.RenameField(
            model_name='mainpagecarousel',
            old_name='carosuelname',
            new_name='carouselname',
        ),
        migrations.AddField(
            model_name='categorylist',
            name='latitude',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorylist',
            name='longitude',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='emailId',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]