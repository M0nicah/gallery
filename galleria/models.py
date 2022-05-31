from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length= 60 )

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    category = models.CharField(max_length=80)

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField( upload_to='gallery/', blank=False, null=True)
    image_name = models.CharField(max_length=40)
    image_description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

   
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['posted_date']


    @classmethod
    def uploaded_images(cls):
        images = cls.objects.filter()
        return images

    @classmethod
    def update_image(cls,pk):
        return cls.objects.get(id=pk)

    @classmethod
    def search_category(cls,search_term):
        images = cls.objects.filter(category__category__icontains=search_term)
        return images

    @classmethod
    def search_location(cls,location):
        locations = cls.objects.filter(location__location__icontains=location)
        return locations
        

