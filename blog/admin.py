from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostModelAdmin(SummernoteModelAdmin):
    fields = ('title', 'text')

admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)
