# Generated by Django 2.0.5 on 2020-02-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]