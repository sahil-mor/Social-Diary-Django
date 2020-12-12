from django.db import models

from datetime import datetime  
# Create your models here.
class ContactAdminData(models.Model) :
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    created_date =  models.DateTimeField(default=datetime.now,blank=True)