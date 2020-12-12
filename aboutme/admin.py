from django.contrib import admin
from django.utils.html import format_html
from .models import AboutMeInfo
# Register your models here.

class AboutMeAdmin(admin.ModelAdmin) :
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('myphoto','description')
    list_display_links = ('myphoto','description')

admin.site.register(AboutMeInfo,AboutMeAdmin)
