from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import display_stories


urlpatterns = [
    path('story/<slug:slug>/', views.StoryDetailView.as_view(), name='stories_detail'),
    path('stories/', display_stories, name='display_stories'), 
    path('', views.StoryList.as_view(), name='home'),  
    path('story/<int:story_id>/submit_comment/', views.submit_comment, name='submit_comment'),
    path('profile/<int:profile_id>/', views.view_profile, name='view_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('submit-story/', views.submit_story, name='submit_story'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
       path('story/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('story/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),

]