from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)


class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('author', 'slug', 'profile_image', 'created_on')
    search_fields = ['author',]
    list_filter = ('updated_on','created_on',)
    prepopulated_fields = {'slug': ('author',)}
