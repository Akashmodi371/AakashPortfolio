from django.contrib import admin
from home.models import Project, Profile, Message, Coding, Descr
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('message', 'desc')
# Register your models here.
admin.site.register(Descr)
admin.site.register(Message, PostAdmin)
admin.site.register(Project, PostAdmin)
admin.site.register(Profile)
admin.site.register(Coding)
