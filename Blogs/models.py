from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  
# Create your models here.
class BlogsModel(models.Model) :
    headline = models.CharField(max_length=255)
    decription = models.CharField(max_length=255)
    num_of_saves = models.IntegerField(default=0)
    owner_user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/blogs/%Y/%m/%d/') 
    created_date = models.DateTimeField(default=datetime.now,blank=True)
