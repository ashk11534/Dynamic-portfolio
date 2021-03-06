# Generated by Django 4.0.3 on 2022-03-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_profile_social_facebook_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user_images/avatar.png', upload_to='user_images'),
        ),
    ]
