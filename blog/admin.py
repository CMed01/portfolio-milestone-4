from django.contrib import admin
from .models import Post, PostComment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title','content']
    list_filter = ('status','created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(PostComment) 
class PostCommentAdmin(SummernoteModelAdmin):
    list_display = ('post', 'author', 'approved', 'created_on')
    search_fields = ['post','body']
    list_filter = ('author','approved','created_on')
    summernote_fields = ('body',)