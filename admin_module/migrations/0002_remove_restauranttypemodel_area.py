# Generated by Django 3.0 on 2020-04-18 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restauranttypemodel',
            name='area',
        ),
    ]
