# Generated by Django 3.1.2 on 2020-10-17 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_test', '0008_remove_chemicalelement_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='EC_MAP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='chemical_manymany',
        ),
        migrations.DeleteModel(
            name='ChmicalPercentage',
        ),
        migrations.AddField(
            model_name='ec_map',
            name='commodity_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mtm', to='sms_test.commodity'),
        ),
        migrations.AddField(
            model_name='ec_map',
            name='element_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mtm', to='sms_test.chemicalelement'),
        ),
    ]
