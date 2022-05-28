from django.test import TestCase

from .models import Image,Category,Location
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
       self.home= Image(name = 'home', user='isaac', image_title='home',image='isaac.png', description='the image is in good condition',size='320px by 210px',image_url='url')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.home,Image))

    # Testing the saved methods
    def test_saved_method(self):
        self.home.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

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
    
    # def test_get_news_today(self):
    #     today_news = Category.todays_news()
    #     self.assertTrue(len(today_news)>0)

    # def test_get_news_by_date(self):
    #     test_date = '2017-03-17'
    #     date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    #     news_by_date = Category.days_news(date)
    #     self.assertTrue(len(news_by_date) == 0)