# Generated by Django 2.0.5 on 2020-04-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='services',
            field=models.ManyToManyField(blank=True, to='status.Service'),
        ),
    ]