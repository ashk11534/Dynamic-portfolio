from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import CV, Profile, Experties, UserMessage, Work
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CVForm, ExpertiesForm, TagForm, UpdateProfileForm, UserMessageForm, WorkForm, UpdateUserForm
import os
from django.http.response import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    try:
        profile = Profile.objects.all().order_by('-id')[0]
    except IndexError:
        return HttpResponse('The server is under maintenance.')
    experties = Experties.objects.all().order_by('-id')
    works = Work.objects.all().order_by('-id')
    user_message_form = UserMessageForm()
    return render(request, 'base/index.html', {
        'profile': profile,
        'experties': experties, 
        'works': works,
        'user_message_form': user_message_form
    })

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            return redirect('user-login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong username or password')
            return redirect('user-login')
    return render(request, 'base/login.html')

@login_required(login_url='user-login')
def update_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    update_profile_form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/update_profile.html', {
        'update_profile_form': update_profile_form 
    })

@login_required(login_url='user-login')
def change_username_email(request):
    user = request.user
    update_user_form = UpdateUserForm(instance=user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('user-login')
    return render(request, 'base/change_username_email.html', {
        'update_user_form': update_user_form
    })

@login_required(login_url='user-login')
def change_password(request):
    user = request.user
    if request.method == 'POST':
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')

        if password_1 == password_2:
            user.set_password(password_1)
            user.save()
            logout(request)
            return redirect('user-login')
        else:
            messages.error(request, "Password didn't match")
            return redirect('change-password')
    return render(request, 'base/change_password.html')

@login_required(login_url='user-login')
def add_experties(request):
    experties_form = ExpertiesForm()
    if request.method == 'POST':
        form = ExpertiesForm(request.POST)
        if form.is_valid():
            experties = form.save(commit=False)
            experties.user = request.user
            experties.save()
            form.save_m2m()
            return redirect('home')
        else:
            experties_form = form
            
    return render(request, 'base/add_experties.html', {
        'experties_form': experties_form 
    })

@login_required(login_url='user-login')
def add_a_new_tag(request):
    tag_form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-experties')
        else:
            tag_form = form
    return render(request, 'base/add_a_new_tag.html', {
        'tag_form': tag_form
    })

@login_required(login_url='user-login')
def update_expertie(request, expertie_id):
    expertie = Experties.objects.get(id=expertie_id)
    experties_form = ExpertiesForm(instance=expertie)
    if request.method == 'POST':
        form = ExpertiesForm(request.POST, instance=expertie)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/update_expertie.html', {
        'experties_form': experties_form 
    })

@login_required(login_url='user-login')
def delete_expertie(request, expertie_id):
    expertie = Experties.objects.get(id=expertie_id)
    if request.method == 'POST':
        delete_expertie = request.POST.get('delete')
        cancel = request.POST.get('cancel')
        if delete_expertie == 'Delete':
            expertie.delete()
            return redirect('home')
        elif cancel == 'Cancel':
            return redirect('home')
    return render(request, 'base/delete_expertie.html', {
        'expertie': expertie
    })
    
@login_required(login_url='user-login')
def add_work(request):
    work_form = WorkForm()
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user
            work.save()
            return redirect('home')
        else:
            work_form = form
            
    return render(request, 'base/add_work.html', {
        'work_form': work_form 
    })

@login_required(login_url='user-login')
def update_work(request, work_id):
    work = Work.objects.get(id=work_id)
    work_form = WorkForm(instance=work)
    if request.method == 'POST':
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/update_work.html', {
        'work_form': work_form 
    })

@login_required(login_url='user-login')
def delete_work(request, work_id):
    work = Work.objects.get(id=work_id)
    if request.method == 'POST':
        delete_work = request.POST.get('delete')
        cancel = request.POST.get('cancel')
        if delete_work == 'Delete':
            work.delete()
            return redirect('home')
        elif cancel == 'Cancel':
            return redirect('home')
    return render(request, 'base/delete_work.html', {
        'work': work
    })

def work_details(request, work_id):
    work = Work.objects.get(id=work_id)
    return render(request, 'base/work_details.html', {
        'work': work
    })

def visitor_message(request):
    if request.method == 'POST':
         form = UserMessageForm(request.POST)
         if form.is_valid():
             form.save()
             messages.success(request, "Message is received by the admin.")
             return redirect('home')

@login_required(login_url='user-login')
def all_messages(request):
    all_messages = UserMessage.objects.filter().order_by('-id')
    return render(request, 'base/messages.html', {
        'all_messages': all_messages
    })

@login_required(login_url='user-login')
def delete_user_message(request, message_id):
    message = UserMessage.objects.get(id=message_id)
    message.delete()
    return redirect('all-messages')

@login_required(login_url='user-login')
def delete_all_user_message(request):
    all_messages = UserMessage.objects.all()
    all_messages.delete()
    return redirect('all-messages')

@login_required(login_url='user-login')
def upload_new_cv(request):
    cv_form = CVForm()
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "CV uploaded successfully.")
            return redirect('home')
        else:
            cv_form = form
    return render(request, 'base/upload_new_cv.html', {
        'cv_form': cv_form
    })


def no_cv_available(request):
    return render(request, 'base/cv_not_available.html')

def download_file(request):
    try:
        uploaded_cv = CV.objects.all().order_by('-id')[0]
    except IndexError:
        return redirect('no-cv-available')
    filename = uploaded_cv.cv.name
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    pdf=open(filepath, 'rb')
    response = HttpResponse(pdf.read(),content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename=%s' % filename
    return response

@login_required(login_url='user-login')
def user_logout(request):
    logout(request)
    return redirect('home')