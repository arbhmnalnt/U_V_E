# Generated by Django 4.2.2 on 2023-06-29 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0006_rent_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='test',
        ),
    ]