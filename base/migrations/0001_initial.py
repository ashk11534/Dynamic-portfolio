# Generated by Django 4.0.3 on 2022-03-08 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=200)),
                ('social_facebook_link', models.CharField(max_length=255, null=True)),
                ('social_linkedin_link', models.CharField(max_length=255, null=True)),
                ('social_instagram_link', models.CharField(max_length=255, null=True)),
                ('social_twitter_link', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(default='base/images/avatar.png', upload_to='user_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
