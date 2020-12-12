from django.contrib import admin
from django.utils.html import format_html
from .models import SaveBlog
# Register your models here.

class SaveModelAdmin(admin.ModelAdmin) :
    def Username(self, obj):
        return obj.user.username
    
    def BlogPhoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.blog.photo.url))
    
    list_display = ('BlogPhoto','Username','savedOn')
    list_display_links = ('Username','BlogPhoto')

admin.site.register(SaveBlog,SaveModelAdmin)