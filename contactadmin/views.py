from django.shortcuts import render,redirect
from django.contrib import messages
from .models import ContactAdminData
from brandInfo.models import BrandIntro
from aboutme.models import AboutMeInfo


brandIntroData = BrandIntro.objects.all()
contactusData = AboutMeInfo.objects.all()

data = {
    'brandIntro' : brandIntroData[0],
    'contactInfo' : contactusData[0],
}

# Create your views here.
def contactus(request) :
    if request.method == 'POST' :
        user_name = request.POST['user_name']
        email = request.POST['email']
        message = request.POST['message']
        new_contact_data = ContactAdminData(user_name=user_name,email=email,message=message)
        new_contact_data.save()
        messages.success(request,"Your data submitted successfully !!!")
        return redirect('contactus')
    else :
        return render(request,'webpages/contactus.html',data)