from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile


@admin.register(Profile)


class ProfileAdmin(SummernoteModelAdmin):
    """Adds summernote functionaility to Profile modal"""
    list_display = ('author', 'slug', 'profile_image', 'created_on',)
    search_fields = ['author',]
    list_filter = ('updated_on', 'created_on',)
    prepopulated_fields = {'slug': ('author',)}
    summernote_fields = ('bio',)    
