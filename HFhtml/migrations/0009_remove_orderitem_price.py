# Generated by Django 3.0.8 on 2020-08-16 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HFhtml', '0008_auto_20200816_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]