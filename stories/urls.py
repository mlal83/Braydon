from . import views
from django.urls import path


urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('<int:stories_id>/', views.story_detail, name='stories_detail'),
]