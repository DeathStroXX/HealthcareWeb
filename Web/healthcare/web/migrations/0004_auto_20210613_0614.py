# Generated by Django 3.1.5 on 2021-06-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210613_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='contact_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
    ]