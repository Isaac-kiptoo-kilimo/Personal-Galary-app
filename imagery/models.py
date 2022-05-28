
from django.db import models

class Image(models.Model):
    name=models.CharField(max_length=100)
    user=models.CharField(max_length=50)
    image_title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image/',null=True)
    description=models.TextField()
    size=models.CharField(max_length=50)
    image_url=models.CharField(max_length=50)
    pub_date=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE,)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        image=Image.objects.filter(id = id).update()
        return image
    
    def get_image_by_id(id):
        images_id=Image.objects.get(image_id = id)
        return images_id

    def search_image(category):
        images=Image.objects.filter(category=category)
        return images

    class Meta:
        ordering = ['name']


    def __str__(self) :
        return self.name

class Location(models.Model):
    distance=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    taken_at=models.CharField(max_length=100)

    def __str__(self) :
        return self.distance


class Category(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=300)

   
    @classmethod
    def search_by_title(cls,search_term):
        categories = cls.objects.filter(title__icontains=search_term)
        return categories
        
    def __str__(self) :
        return self.title