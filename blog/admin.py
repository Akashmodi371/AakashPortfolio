from django.contrib import admin
from blog.models import Post, BlogComment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'desc')


admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment)
