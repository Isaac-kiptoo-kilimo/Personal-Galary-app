
from django.db import models

class Image(models.Model):
    name=models.CharField(max_length=100)
    image_post=models.ImageField(upload_to='image/',null=True)
    description=models.TextField()
    location=models.ForeignKey('Location',on_delete=models.CASCADE,)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Location(models.Model):
    distance=models.CharField(max_length=50)

    def __str__(self) :
        return self.distance


class Category(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=300)
    
    def __str__(self) :
        return self.name