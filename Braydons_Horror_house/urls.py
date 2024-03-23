
from django.contrib import admin 
from django.urls import path, include
from stories import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stories.urls')),  
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('profile/', views.profile_view, name='profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),

]
