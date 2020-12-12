from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.saveBlog,name='saveBlog'),
]