from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.create_comment,name='create_comment' ),
    path('delete_comment/<int:blogId>/<int:cmtId>/',views.delete_comment,name='delete_comment' ),
]