from django.shortcuts import render, redirect
from django.http import HttpResponse
from galleria.models import Image, Location, Category
# Create your views here.

def gallery(request):
    message = 'unsplash like gallery'
    images = Image.uploaded_images()
    return render(request, 'galleria/gallery.html', {'message':message, 'images':images})


