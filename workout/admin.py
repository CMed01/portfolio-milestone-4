from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Workout, WorkoutComment


@admin.register(Workout)
class WorkoutAdmin(SummernoteModelAdmin):
    """Adds summernote functionaility to Workout modal"""
    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content', ]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('workout',)
    

admin.site.register(WorkoutComment)
