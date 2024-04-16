from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, Header

# Register your models here.

admin.site.register(Header)

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on','status')
    summernote_fields = ('content',)
