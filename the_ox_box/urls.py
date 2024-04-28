"""
URL configuration for the_ox_box project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls, name='admin'),
    path('blog/', include("blog.urls"), name='blog-urls'),
    path('profile/', include("userprofile.urls"), name='userprofile-urls'),
    path('summernote/', include('django_summernote.urls')),
    path('workout/', include("workout.urls"), name='workout-urls'),
    path('', include("about.urls"), name='about-urls'),
]

# Error handler, custom page views

handler400 = 'the_ox_box.views.custom_400'
handler403 = 'the_ox_box.views.custom_403'
handler404 = 'the_ox_box.views.custom_404'
