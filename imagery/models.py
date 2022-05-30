

from django.db import models

class Image(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',null=True)
    description=models.TextField()
    size=models.CharField(max_length=50) 
    pub_date=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE,)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    
    def delete_image(self):
        self.save_image()
        self.delete()
    
    def update_image(self,img):
        image=Image.objects.get(id = id)
        image.name=img.name
        image.image=img.image
        image.description=img.description
        image.save()
        return image

    @classmethod
    def search_by_category(cls,search_term):
        searched_images = cls.objects.filter(category__category__icontains=search_term)
        return searched_images
    
    def get_image_by_id(id):
        images_id=Image.objects.get(image_id = id)
        return images_id

    def search_image(category):
        images=Image.objects.filter(category=category)
        return images

    class Meta:
        ordering = ['-id']


    def __str__(self) :
        return self.name

class Location(models.Model):
    place=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.place


class Category(models.Model):
    category=models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.save_category()
        self.delete()
    
    def get_all_category(self):
        self.save_category()
        
    @classmethod
    def update_category(cls,id,category):
        category=cls.objects.filter(id=id).update(category=category)
        return category

    def __str__(self) :
        return self.title