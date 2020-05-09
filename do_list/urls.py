from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home') , 
path('about/',views.about,name='about') ,
path('delete/<list_id>',views.delete,name='delete'),
path('status/<list_id>',views.status,name='status'),
path('unstatus/<list_id>',views.unstatus,name='unstatus')
   
]