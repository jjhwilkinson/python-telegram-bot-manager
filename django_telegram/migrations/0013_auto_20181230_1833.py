# Generated by Django 2.1.2 on 2018-12-30 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_telegram', '0012_auto_20181230_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sent_to_bot',
            new_name='sent_to_bots',
        ),
    ]