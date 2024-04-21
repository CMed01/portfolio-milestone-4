from django.contrib import admin
from .models import Workout, WorkoutComment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Workout)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title','content']
    list_filter = ('status','created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('workout',)

admin.site.register(WorkoutComment)