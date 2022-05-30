from django.test import TestCase

from .models import Image,Category,Location
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
       self.home= Image(id=1,name = 'home', image='isaac.png', description='the image is in good condition',size='320px by 210px',pub_date='25-11-2021',Location='Eldoret')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.home,Image))

    # Testing the saved methods
    def test_saved_method(self):
        self.home.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

# class ImageTestClass(TestCase):
#     def setUp(self):
#         self.location = Location(name='Nairobi')
#         self.location.save_location()

#         self.category = Category(name='Travel')
#         self.category.save_category()

        

#         self.image_test = Image(id=1, name='photo', description='this is a image', image='image',image_url='url', location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'images/test.jpg')
        new_image = Image.objects.filter(image='images/test.jpg')
        self.assertTrue(len(new_image) > 0)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        images = self.image_test.filter_by_location(location='Eldoret')
        self.assertTrue(len(images) == 1)

    def test_search_image_by_category(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_category(category='Travel')
        self.assertTrue(len(found_images) == 1)

class CategoryTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.home= Image(name = 'home', user='isaac', image_title='home',description='the image is in good condition',size='320px by 210px',image_url='url')
        self.home.save_image()

        # Creating a new tag and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save()

        self.new_category= Category(title = 'Test Article',post = 'This is a random test Post',image = self.james)
        self.new_category.save()

        self.new_category.location.add(self.new_location)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
    
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(name='Travel')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

