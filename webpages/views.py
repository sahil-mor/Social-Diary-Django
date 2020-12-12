from django.shortcuts import render
from brandInfo.models import BrandIntro
from Blogs.models import BlogsModel
from aboutme.models import AboutMeInfo
# Create your views here.
brandIntroData = BrandIntro.objects.all()
contactusData = AboutMeInfo.objects.all()
blogsData = BlogsModel.objects.order_by('-num_of_saves')

data = {
    'brandIntro' : brandIntroData[0],
    'contactInfo' : contactusData[0],
    'blogsData' : blogsData
}

def home(request) :
    return render(request,'webpages/home.html',data)

