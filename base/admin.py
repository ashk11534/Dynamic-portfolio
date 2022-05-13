from django.contrib import admin
from django.test import tag

# Register your models here.

from .models import Profile, Experties, Work, UserMessage, Tag, CV

admin.site.register(Profile)
admin.site.register(Experties)
admin.site.register(Work)
admin.site.register(UserMessage)
admin.site.register(Tag)
admin.site.register(CV)