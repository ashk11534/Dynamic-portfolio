# Generated by Django 4.0.3 on 2022-03-11 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_experties_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='user',
        ),
    ]
