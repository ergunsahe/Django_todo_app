# Generated by Django 3.1.4 on 2020-12-28 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('-created_date',)},
        ),
    ]
