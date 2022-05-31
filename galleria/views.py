from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from galleria.models import Image, Location, Category
from galleria.forms import ImageForm
# Create your views here.

def gallery(request):
    images = Image.uploaded_images()
    
    return render(request, 'galleria/gallery.html', {'images':images})

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

    
def search_image(request):
    if 'q' in request.GET and request.GET["category"]:             #checks if the query exists in the request .get method then check if it has a value
        search_term = request.GET.get("category")                        #then we get the search term using the method called on the request.get object
        searched_categories = Image.search_category(search_term)        #calling the searched articles and passing in the input(search_term). if articles of the input is found it is rendered in th html.
        message = f"{search_term}"

        return render(request, 'galleria/search.html',{"message":message, "images": searched_categories})
 #if the condition is not met we pass in an error message to inform the user what went wrong

    else:
        message = "You haven't searched for any term"
        return render(request, 'galleria/search.html',{"message":message})

def filter_by_location(request):
    if 'q' in request.GET and request.GET["location"]:             #checks if the query exists in the request .get method then check if it has a value
        location = request.GET.get("location")                        #then we get the search term using the method called on the request.get object
        searched_locations = Image.search_location(location)        #calling the searched articles and passing in the input(search_term). if articles of the input is found it is rendered in th html.
        message = f"{location}"

        return render(request, 'galleria/locations.html',{"message":message, "locations": searched_locations})
 #if the condition is not met we pass in an error message to inform the user what went wrong

    else:
        message = "You haven't searched for any term"
        return render(request, 'galleria/locations.html',{"message":message})

