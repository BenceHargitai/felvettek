# Generated by Django 3.1.7 on 2021-03-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('felvevo', '0004_auto_20210310_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanuló',
            name='szak',
            field=models.CharField(max_length=30),
        ),
    ]