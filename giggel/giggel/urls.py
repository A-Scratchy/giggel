"""giggel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from user import views as user_views
from django_registration.backends.activation.views import RegistrationView
from user.forms import RegistrationForm

urlpatterns = [
    path('blankPage/', main_views.blankPage, name='blankPage'),
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('register/', RegistrationView.as_view(form_class=RegistrationForm),
         name='register'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', user_views.profile, name='profile'),
    path('profile/update', user_views.updateProfile, name='updateProfile'),
    path('testEmail/', user_views.testEmail, name='testEmail'),
]
