# Generated by Django 4.0.6 on 2022-10-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='goal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]