# Generated by Django 2.1.2 on 2019-01-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_telegram', '0023_handler_filter_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='handlerinstance',
            name='add_order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]