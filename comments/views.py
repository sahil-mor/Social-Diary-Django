from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Blogs.models import BlogsModel
from .models import UserComments
# Create your views here.

@login_required(login_url='signin')
def create_comment(request,id):
    if request.method == 'POST':
        comment = request.POST['comment']
        blog = get_object_or_404(BlogsModel,pk=id)
        new_comment = UserComments.objects.create(user=request.user,blog=blog,comment=comment)
        new_comment.save()
        messages.success(request,'Comment added successfully !!!')
        requiredUrl = '/blogs/' + str(id)
        return redirect(requiredUrl)
    else :
        return redirect('home')

@login_required(login_url='signin')
def delete_comment(request,blogId,cmtId) :
    required_comment = get_object_or_404(UserComments,pk=cmtId)
    required_blog = get_object_or_404(BlogsModel,pk=blogId)
    if required_comment.user.id == request.user.id or request.user.id == required_blog.owner_user_id : 
        deleted = UserComments.objects.filter(blog_id=blogId,id=cmtId).delete()
        messages.success(request,'Comment deleted successfully !!!')
    
    requiredUrl = '/blogs/' + str(blogId)
    return redirect(requiredUrl)