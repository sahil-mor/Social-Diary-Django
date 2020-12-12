from django.db import models

# Create your models here.
class BrandIntro(models.Model):
    welcomeMsg = models.CharField(max_length=255)
    brandName = models.CharField(max_length=255)
    highlightMsg = models.TextField()
    backgroundVideo = models.FileField(upload_to='uploads/videos/%Y/%m/%d/', null=True, verbose_name="")