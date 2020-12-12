from django.db import models
from django.contrib.auth.models import User
from Blogs.models import BlogsModel
from datetime import datetime  
# Create your models here.

class SaveBlog(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogsModel,on_delete=models.CASCADE)
    savedOn = models.DateTimeField(default=datetime.now,blank=True)
    