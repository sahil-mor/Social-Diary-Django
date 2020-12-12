from django.db import models
from django.contrib.auth.models import User
from Blogs.models import BlogsModel
from datetime import datetime  

# Create your models here.

class UserComments(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogsModel,on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now,blank=True)
    