from django.shortcuts import render
from .models import Photo

def list_image(request):
    images = Photo.objects.all()
    return render(request, 'photo/image_list.html', {'images': images})
