from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Func, F, Count
from django.contrib import messages
from .forms import BlogsForm
from itertools import chain

from savedby.models import SaveBlog
from Blogs.models import BlogsModel
from brandInfo.models import BrandIntro
from comments.models import UserComments
from aboutme.models import AboutMeInfo
# Create your views here.

brandIntroData = BrandIntro.objects.all()
contactusData = AboutMeInfo.objects.all()
data = {
    'brandIntro' : brandIntroData[0],
    'contactInfo' : contactusData[0]
}

def allBlogs(request) :
    blogsData = BlogsModel.objects.order_by('-created_date')
    data['blogsData'] = blogsData
    return render(request,'Blogs/allBlogs.html',data)

def blogInfo(request,id) :
    # blogData = get_object_or_404(BlogsModel,pk=id)
    blogData = BlogsModel.objects.filter(id=id).annotate(createAtDate=Func(F('created_date'), function='date'))
    comments = UserComments.objects.filter(blog_id=id)
    if request.user.is_authenticated :
        isSaved = SaveBlog.objects.filter(user_id=request.user.id , blog_id=id)
        if isSaved :
            data['whatToWrite'] = 'Saved'
        else :
            data['whatToWrite'] = 'Save'
    else :
        data['whatToWrite'] = 'Saves'
    data['blogData'] = blogData[0]
    data['comments'] = comments
    return render(request,'Blogs/blogDetail.html',data)

# redirect user to login if user is not logged in

@login_required(login_url='signin')
def create(request) :
    if request.method == 'POST':
        form = BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner_user = request.user
            obj.save()
            
        messages.success(request,"Blog created successfully")
        return redirect('dashboard')
    else :
        return redirect('dashboard')

def deleteBlog(request,id) :
    required_blog = get_object_or_404(BlogsModel,pk=id)
    if required_blog.owner_user_id == request.user.id :
        deletedComments = UserComments.objects.filter(blog_id=id).delete()
        deleted = BlogsModel.objects.filter(id=id).delete()
        messages.warning(request,"Blog deleted successfully")


    return redirect('dashboard')
    