from django.shortcuts import render
from .models import Image,Location,Category
from django.http import Http404
def index(request):
    try:
        image=Image.objects.all()
    except Image.DoesNotExist:
        raise Http404()  
    return render (request,'pages/index.html',{"images":image})

def get_images(request):
    try:
        image=Image.objects.all()
    except Image.DoesNotExist:
        raise Http404()
    return render (request,'pages/images.html',{"images":image} )

def get_single_image(request):
    return render (request,'pages/single.html')

def addimage(request):
    return render(request,'pages/addimage.html')

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'pages/search.html',{"message":message,"categories":searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'pages/search.html',{"message":message})

# def article(request,article_id):
#     try:
#         article = Article.objects.get(id = article_id)
#     except Article.DoesNotExist:
#         raise Http404()
#     return render(request,"all-news/article.html", {"article":article})