# Generated by Django 3.0.7 on 2020-07-17 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0047_auto_20200717_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='sub_service',
        ),
        migrations.AddField(
            model_name='ticket',
            name='sub_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='status.SubService', verbose_name='Sub-Service'),
        ),
    ]