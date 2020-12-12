from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout

from brandInfo.models import BrandIntro
from savedby.models import SaveBlog
from Blogs.forms import BlogsForm
from Blogs.models import BlogsModel
from aboutme.models import AboutMeInfo
# Create your views here.

brandIntroData = BrandIntro.objects.all()
contactusData = AboutMeInfo.objects.all()
data = {
    'brandIntro' : brandIntroData[0],
    'contactInfo' : contactusData[0]
}

def signin(request) :
    if request.user.is_authenticated :
        return redirect('home')
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None :
            auth.login(request,user)
            print(user.is_superuser)
            return redirect('home')
        else :
            messages.warning(request, "Username or password is wrong" )
            return redirect('signin')
    else :
        return render(request,'accounts/signin.html',data)
   

def signup(request) :
    if request.user.is_authenticated :
        return redirect('home')
    if request.method == 'GET' :
        return render(request,'accounts/signup.html',data)
    elif request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword :
            if User.objects.filter(username=username ).exists():
                messages.warning(request, "Username already taken !!!" )
                return redirect('signup')
            else :
                if User.objects.filter(email=email).exists():
                    messages.warning(request, "Email already taken !!!" )
                    return redirect('signup')
                else :
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save() # save user in database
                    messages.success(request, "Account created successfully" ) # flash messages
                    return redirect('signin')
        else :
            messages.warning(request, "Password do not match" )
            return redirect('signup')
        return render(request,'accounts/signup.html',data)


@login_required(login_url='signin')
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='signin')
def dashboard(request) :
    savedBlogs = SaveBlog.objects.filter(user_id=request.user.id).order_by('-savedOn')
    createdBlogs = BlogsModel.objects.filter(owner_user_id=request.user.id).order_by('-created_date')
    form = BlogsForm()
    data['savedBlogs'] = savedBlogs
    data['createdBlogs'] = createdBlogs
    print(createdBlogs)
    data['form'] = form
    return render(request,'accounts/dashboard.html',data)
