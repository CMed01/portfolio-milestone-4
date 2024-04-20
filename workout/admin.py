from django.contrib import admin
from .models import Workout, WorkoutComment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Workout)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('wodtitle', 'slug', 'status', 'created_on')
    search_fields = ['wodtitle','content']
    list_filter = ('status','created_on',)
    prepopulated_fields = {'slug': ('wodtitle',)}
    summernote_fields = ('workout',)

admin.site.register(WorkoutComment)