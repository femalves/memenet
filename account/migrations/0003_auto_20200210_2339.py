# Generated by Django 2.0.5 on 2020-02-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='static/img/pic.png', upload_to='users/%Y/%m/%d'),
        ),
    ]
