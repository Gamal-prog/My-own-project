from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def list_image(request):
    images = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'image': image})

def image_new(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.author = request.user
            form.save()
            return redirect('image_list')
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_new.html', {'image_form': form})

def image_edit(request, pk):
    image = get_object_or_404(Photo, pk=pk)
    form = PhotoForm(request.POST or None, request.FILES or None, instance=image)
    if form.is_valid():
        form.save()
        return redirect('image_list')
    else:
        form = PhotoForm(request.POST or None, instance=image)
    return render(request, 'photo/photo_edit.html', {'image': image, 'form': form})

def image_delete(request, pk):
    image = get_object_or_404(Photo, pk=pk)
    image.delete()
    return redirect('image_list')

#####################users 

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'photo/register.html', {'reg_form': form})

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







'''
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
'''