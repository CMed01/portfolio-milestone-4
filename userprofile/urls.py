from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_profile, name='profile'),
    path('<slug:slug>',
         views.edit_profile, name='profile_edit'),
]
