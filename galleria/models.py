from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    spot_name = models.CharField(max_length= 60, default='')

    def __str__(self):
        return self.spot_name

class Category(models.Model):
    section_name = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.section_name

class Image(models.Model):
    image = models.ImageField(blank=False, null=False)
    image_name = models.CharField(max_length=40)
    image_description = models.TextField()
    spot_name = models.ForeignKey(Location, on_delete=models.DO_NOTHING, default='')
    section_name = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default='')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

