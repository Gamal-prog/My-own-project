from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def register_users(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(username=username)
            login(request, user)
            return redirect('image_list')
    else:
        user_form = UserCreationForm()

    return render(request, 'auth', {'regis_form': user_form})
