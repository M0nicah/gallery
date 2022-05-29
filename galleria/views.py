from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from galleria.models import Image, Location, Category
from galleria.forms import ImageForm
# Create your views here.

def gallery(request):
    image = Image.uploaded_images()
    return render(request, 'galleria/gallery.html', {'images':image})

def add_image(request):
    category = Category.objects.all()
    location = Location.objects.all()

    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gallery')

    return render(request, 'galleria/image_form.html', {'form':form,'category':category, 'location':location })

def update_image(request, pk):
    categories = Category.objects.all()
    locations = Location.objects.all()

    image = Image.update_image(pk)
    form = ImageForm(instance=image)
    if request.method == "POST":
        form = ImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            return redirect('gallery')

    return render(request, 'galleria/image_form.html', { 'form': form, 'categories':categories, 'locations':locations } )

def delete_image(request, pk):
    image = Image.objects.get(id=pk)
    
    if request.method == 'POST':
        image.delete_image()
        return redirect('gallery')

    return render(request, 'galleria/delete.html', {'image':image})

def search_results(request):
   x = request.GET.get('x') if request.GET.get('x') != None else ''
   images = Image.search_image(category=x) or Image.filter_by_location(location=x)

   return render(request, 'galleria/gallery.html', {'images':images})


