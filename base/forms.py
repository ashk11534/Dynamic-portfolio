from django import forms
from .models import CV, Experties, Tag, Work, Profile, UserMessage
from django.contrib.auth.models import User

class ExpertiesForm(forms.ModelForm):
    class Meta:
        model = Experties
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-transparent text-light'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control bg-transparent text-light'}),  
        }

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-transparent text-light'}), 
            'github_link': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
            'live_site_link': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
        }

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
            'designation': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}), 
            'description': forms.Textarea(attrs={'class': 'form-control bg-transparent text-light'}),
            'social_facebook_link': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
            'social_linkedin_link': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
            'social_instagram_link': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
            'social_twitter_link': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
        }

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-transparent text-light'}),   
        }

class UserMessageForm(forms.ModelForm):
    class Meta:
        model =  UserMessage
        fields = '__all__'
        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Enter your name'}),
            'sender_email': forms.EmailInput(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Enter your email'}),
            'sender_message': forms.Textarea(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write your message here...'}),

        }

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields='__all__'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}),
        }