# Generated by Django 3.1.5 on 2021-06-13 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20210613_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='clinic',
        ),
    ]
