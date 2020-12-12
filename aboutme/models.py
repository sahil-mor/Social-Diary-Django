from django.db import models

# Create your models here.
class AboutMeInfo(models.Model) :
    photo = models.ImageField(upload_to='uploads/aboutme/%Y/%m/%d/')
    description = models.TextField()
    insta_link = models.CharField(max_length=255)
    linkedin_link = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    website_link = models.CharField(max_length=255) 
    address = models.CharField(max_length=255, default='#' ) 
    phone = models.CharField(max_length=255, default='#' ) 
    email = models.CharField(max_length=255, default='#' ) 