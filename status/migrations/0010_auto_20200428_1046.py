# Generated by Django 3.0.5 on 2020-04-28 14:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('status', '0009_auto_20200428_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='category_status',
            new_name='status',
        ),
    ]
