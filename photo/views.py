from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def list_image(request):
    images = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'image': image})

def image_new(request):
    form = PhotoForm()
    return render(request, 'photo/photo_edit.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password,)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('image_list')
        else:
            messages.success(request, ("Try again, please"))
            return redirect('login')
    else:
        return render(request, 'photo/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('image_list')



'''def photo_edit(request, pk):
    image = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=image)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.save()
            return redirect('photo_detail', pk=image.pk)
        else:
         form = PhotoForm(instance=image)
    return render(request, 'blog/photo_edit.html', {'form': form})'''

'''if request.method == "POST":
        if 'save' in request.POST:
            form = PhotoForm(request.POST)
            form.save()'''


'''def image_new(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.save()
            return redirect('photo_detail', pk=image.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_edit.html', {'form': form})'''