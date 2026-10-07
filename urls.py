from django.urls import path
from .views import register_user, login_user, post_job, get_jobs, apply_job, get_applications

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('post-job/', post_job, name='post_job'),
    path('jobs/', get_jobs, name='get_jobs'),
    path('apply-job/', apply_job, name='apply_job'),
    path('applications/', get_applications, name='get_applications'),

]