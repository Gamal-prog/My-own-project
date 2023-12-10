from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.list_image, name='image_list'),
    path('photo/<int:pk>/', views.image_detail, name='image_detail'),
    path('photo/new/', views.image_new, name='image_new'),
    path('photo/<int:pk>/edit/', views.image_edit, name='image_edit'),
    path('photo/<int:pk>/delete', views.image_delete, name='image_delete'),
    #users
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)