from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    social_facebook_link = models.CharField(max_length=255, null=True, blank=True)
    social_linkedin_link = models.CharField(max_length=255, null=True, blank=True)
    social_instagram_link = models.CharField(max_length=255, null=True, blank=True)
    social_twitter_link = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='user_images', default='user_images/avatar.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Experties(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image =  models.ImageField(upload_to='project_images')
    github_link = models.CharField(max_length=255, null=True, blank=True)
    live_site_link = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserMessage(models.Model):
    sender_name = models.CharField(max_length=200)
    sender_email = models.EmailField()
    sender_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sender_name

class CV(models.Model):
    cv = models.FileField(upload_to='cv')

    def __str__(self):
        return self.cv.name

