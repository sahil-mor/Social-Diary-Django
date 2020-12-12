from django.contrib import admin
from django.utils.html import format_html
from .models import UserComments
# Register your models here.

class UserCommentsAdmin(admin.ModelAdmin) :
    def Username(self, obj):
        return obj.user.username
    
    def BlogPhoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.blog.photo.url))
    
    list_display = ('BlogPhoto','Username','comment','created_date')
    list_display_links = ('Username','BlogPhoto')

admin.site.register(UserComments,UserCommentsAdmin)