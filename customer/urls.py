from . import views
from django.urls import path

urlpatterns = [
    path('registeration/', views.register_users, name='register_user'),
]
