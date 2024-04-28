from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, ContactRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """Adds summernote functionaility to admin modal"""
    list_display = ('title', 'updated_on',)
    search_fields = ['title', 'content',]
    list_filter = ('updated_on', 'status',)
    summernote_fields = ('content',)


admin.site.register(ContactRequest)
