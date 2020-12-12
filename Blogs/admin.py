from django.contrib import admin
from django.utils.html import format_html
from .models import BlogsModel
# Register your models here.

class BlogsModelAdmin(admin.ModelAdmin) :
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('owner_user','headline','myphoto')
    list_display_links = ('headline',)

admin.site.register(BlogsModel,BlogsModelAdmin)
