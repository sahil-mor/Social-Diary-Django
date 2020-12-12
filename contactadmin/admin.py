from django.contrib import admin
from .models import ContactAdminData
# Register your models here.

class ContactAdminView(admin.ModelAdmin) :
    list_display = ('user_name','email','message','created_date')
    list_display_links = ('user_name',)

admin.site.register(ContactAdminData,ContactAdminView)
