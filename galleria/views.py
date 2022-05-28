from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def gallery(request):
    message = 'unsplash like gallery'
    return render(request, 'galleria/gallery.html', {'message':message})
