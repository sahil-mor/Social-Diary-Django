from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import SaveBlog
from Blogs.models import BlogsModel

# Create your views here.

@login_required(login_url='signin')
def saveBlog(request,id) :
    isSaved = SaveBlog.objects.filter(user_id=request.user.id , blog_id=id)
    blog = get_object_or_404(BlogsModel,pk=id)
    
    if isSaved :
        deleted = SaveBlog.objects.filter(user_id=request.user.id , blog_id=id).delete()
        blog.num_of_saves -= 1
        messages.warning(request, "Removed from saved blogs successfully" )
    else :
        newSave = SaveBlog.objects.create(user=request.user,blog=blog)
        newSave.save()
        blog.num_of_saves += 1
        messages.success(request, "Blog saved successfully" )
    blog.save()
    requiredUrl = '/blogs/' + str(id)
    return redirect(requiredUrl)