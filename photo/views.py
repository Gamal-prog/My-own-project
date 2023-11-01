from django.shortcuts import render
from .models import Photo

def list_image(request):
    images = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'images': images})

def image_detail(request):
    image = Photo.objects.get()
    return render(request, 'photo/photo_detail.html', {'image': image})