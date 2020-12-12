from django.shortcuts import render
from .models import AboutMeInfo
# Create your views here.

from brandInfo.models import BrandIntro

# Create your views here.
brandIntroData = BrandIntro.objects.all()
contactusData = AboutMeInfo.objects.all()


data = {
    'brandIntro' : brandIntroData[0],
    'contactInfo' : contactusData[0]
}

def aboutme(request) :
    aboutMeData = AboutMeInfo.objects.all()
    data['aboutMeData'] = aboutMeData[0]
    return render(request,'webpages/aboutme.html',data)
