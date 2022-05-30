from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.

class ImageTestCase(TestCase):
    # setup method
    def setUp(self) -> None:
        self.image = Image(image_name="my photo", image_description="My favourite image")

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        '''
        test_delete_image test case to test if the image object is removed from
        the db.
        '''

        self.image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)


class LocationTestCase(TestCase):

    def setUp(self) -> None:
        self.location = Location(location="Diani Beach")

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        '''
        test_save_image test case to test if the image object is added to
        the db.
        '''
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        

    def test_delete_method(self):
        '''
        test_delete_image test case to test if the image object is removed from
        the db.
        '''
        
        # location
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)

        # category
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)