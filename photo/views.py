from django.shortcuts import render, get_object_or_404
from .models import Photo

def list_image(request):
    images = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'image': image})