from .views import (home_view, contact_us_view, submit_request,
                    about_us_view, projects_view, success_view, TelegramUserCreateAPIView)
from django.urls import path

urlpatterns = [
    path('', home_view, name='home_view'),
    path('contact-us', contact_us_view, name='contact_us_view'),
    path('submit-request', submit_request, name='submit_request'),
    path('about-us', about_us_view, name='about_us_view'),
    path('projects', projects_view, name='projects_view'),
    path('success', success_view, name='success_view'),
    path('api/v1/create-telegram-bot', TelegramUserCreateAPIView.as_view())
]
