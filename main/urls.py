from django.contrib.auth import views as auth_views
from django.urls import path

from main.views import landingPageView, login_view

app_name = 'main'

urlpatterns = [
    path('', landingPageView, name='main'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]