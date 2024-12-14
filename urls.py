from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="Home"),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('pet/<int:id>', singlepet, name="Single-Pet"),

    path('pets/create/', pet_create, name='pet_create'),
    path('pets/<int:pk>/update/', pet_update, name='pet_update'),
    path('pets/<int:pk>/delete/', pet_delete, name='pet_delete'),

    path('profile/self/', self_profile_view, name='self_profile'),
    path('profile/<str:username>/', profile_view, name='profile'),

    path('pets/all/', all_pets_view, name='all_pets'),
    
    path('adopt/<int:id>', adopt, name="adoption"),
    path('myadoption/', myadoptions, name='my-adoption'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


