# Generated by Django 3.1.2 on 2020-10-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_test', '0009_auto_20201017_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicalelement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
