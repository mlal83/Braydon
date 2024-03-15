from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('set_avatar/', views.set_avatar, name='set_avatar'),
    path('<slug:slug>/', views.post_detail, name="stories_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('submit-story/', views.submit_story, name='submit_story'),
    path('upload-profile-picture/', views.profile_picture_upload, name='profile_picture_upload'),  # Updated line
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
]
