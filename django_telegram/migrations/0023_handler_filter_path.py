# Generated by Django 2.1.2 on 2019-01-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_telegram', '0022_auto_20190106_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='handler',
            name='filter_path',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
