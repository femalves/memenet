# Generated by Django 2.0.5 on 2020-02-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200210_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='img/pic.png', upload_to='users/%Y/%m/%d'),
        ),
    ]
