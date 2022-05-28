from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length= 60 )

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=80)

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField( upload_to='gallery/', blank=False, null=False)
    image_name = models.CharField(max_length=40)
    image_description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    category = models.ManyToManyField(Category)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

   
    def save_image(self):
        self.save()

    class Meta:
        ordering = ['image_name']
  

