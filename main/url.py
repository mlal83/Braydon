from . import views
from django.urls import path, include
urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path("about/", include("about.urls"), name="about-urls"),    
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('events/', views.EventList.as_view(), name='events'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path('articles/<slug:slug>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
    path('articles/<slug:slug>/delete_comment/<int:comment_id>',views.comment_delete, name='comment_delete'),
    path('events/<slug:slug>/edit_review/<int:review_id>',views.review_edit, name='review_edit'),
    path('events/<slug:slug>/delete_review/<int:review_id>',views.review_delete, name='review_delete'),
]