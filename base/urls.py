from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user-login', views.user_login, name='user-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('update-profile/<int:profile_id>', views.update_profile, name='update-profile'),
    path('change-username-email', views.change_username_email, name='change-username-email'),
    path('change-password', views.change_password, name='change-password'),
    path('add-experties', views.add_experties, name='add-experties'),
    path('add-work', views.add_work, name='add-work'),
    path('work-details/<int:work_id>', views.work_details, name='work-details'),
    path('update-expertie/<int:expertie_id>', views.update_expertie, name="update-expertie"),
    path('update-work/<int:work_id>', views.update_work, name="update-work"),
    path('delete-expertie/<int:expertie_id>', views.delete_expertie, name="delete-expertie"),
    path('delete-work/<int:work_id>', views.delete_work, name="delete-work"),
    path('visitor-message', views.visitor_message, name='visitor-message'),
    path('all-messages', views.all_messages, name='all-messages'),
    path('delete-user-message/<int:message_id>', views.delete_user_message, name='delete-user-message'),
    path('delete-all-user-message', views.delete_all_user_message, name='delete-all-user-message'),
    path('upload-new-cv', views.upload_new_cv, name='upload-new-cv'),
    path('download', views.download_file, name='download'),
    path('no-cv-available', views.no_cv_available, name='no-cv-available'),
    path('add-a-new-tag', views.add_a_new_tag, name='add-a-new-tag')
]