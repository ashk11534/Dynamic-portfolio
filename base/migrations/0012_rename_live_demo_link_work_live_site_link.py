# Generated by Django 4.0.3 on 2022-03-10 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_work_github_link_work_live_demo_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='live_demo_link',
            new_name='live_site_link',
        ),
    ]
