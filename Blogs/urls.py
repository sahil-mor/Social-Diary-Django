from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.allBlogs,name='blogs') ,
    path('create',views.create,name='create_blog') ,
    path('<int:id>',views.blogInfo,name='blog' ),
    path('delete/<int:id>',views.deleteBlog,name='deleteBlog' ),
]