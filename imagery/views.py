
from unicodedata import category
from django.shortcuts import render
from .models import Image,Location,Category
from django.http import Http404
from PIL import Image as PILimage
def index(request):
    images=Image.objects.all()
   
    return render (request,'pages/index.html',{"images":images})




def addimage(request):
    locations=Location.objects.all()
    categories=Category.objects.all()
    if request.method=='POST':
        image=request.FILES.get('photo')
        image_=PILimage.open(image)
        name=request.POST.get('name')
        size=f'{image_.width} x {image_.height}'
        description=request.POST.get('description')
        category=request.POST.get('category')
        category_=Category.objects.get(id=category)
        location=request.POST.get('location')
        location_=Location.objects.get(id=location)
        img=Image(name=name,image=image,description=description,size=size,location=location_,category=category_)
        img.save_image()
    return render(request,'pages/addimage.html',{"categories":categories,"locations":locations})

def search_results(request):
    locations=Location.objects.all()
    categories=Category.objects.all()
    if 'category' in request.GET and request.GET["category"]:
        cat= request.GET.get("category")
        category=Category.objects.get(id=cat)
        images=Image.objects.filter(category=category)
        return render(request, 'pages/search.html',{"locations":locations,"categories":categories,"images":images})
    if 'location' in request.GET and request.GET["location"]:
        loc= request.GET.get("location")
        location=Location.objects.get(id=loc)
        images=Image.objects.filter(location=location)
        return render(request, 'pages/search.html',{"locations":locations,"categories":categories,"images":images})
 
    return render(request, 'pages/search.html',{"locations":locations,"categories":categories})

def search(request):
       if 'image' in request.GET and request.GET["image"]:
        search_term=request.GET.get("image")
        searched_images=Image.search_by_category(search_term)
        message=f"{search_term}"
        return render(request, 'pages/search.html',{"message":message,"images": searched_images})
        