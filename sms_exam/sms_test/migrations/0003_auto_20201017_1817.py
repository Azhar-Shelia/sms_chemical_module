# Generated by Django 3.1.2 on 2020-10-17 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_test', '0002_chmicalpercentage_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chmicalpercentage',
            old_name='name',
            new_name='name_1',
        ),
    ]
