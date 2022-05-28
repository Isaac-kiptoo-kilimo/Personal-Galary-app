from django.shortcuts import render

def index(request):
    return render (request,'pages/index.html')

def get_images(request):
    return render (request,'pages/images.html')

def get_single_image(request):
    return render (request,'pages/single.html')

def addimage(request):
    return render(request,'pages/addimage.html')