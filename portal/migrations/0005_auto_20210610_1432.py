# Generated by Django 3.1.7 on 2021-06-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20210610_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Street_name',
            field=models.TextField(default='Morison Crescent', max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='Street_number',
            field=models.CharField(default='No 58B', max_length=250),
        ),
    ]