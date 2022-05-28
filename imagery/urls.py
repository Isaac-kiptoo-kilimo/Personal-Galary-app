from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('images/',views.get_images,name='images'),
    path('image/',views.get_single_image,name='image'),
    path('addimage/',views.addimage,name='addimage'),
]