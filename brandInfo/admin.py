from django.contrib import admin
from .models import BrandIntro
# Register your models here.

class BrandIntroAdmin(admin.ModelAdmin) :
    list_display = ('brandName','welcomeMsg', 'highlightMsg' )
    list_display_links = ('brandName',)

admin.site.register(BrandIntro,BrandIntroAdmin)
