from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
RATING = ((1, "1 Star"), (2, "2 Stars"), (3, "3 Stars"), (4, "4 Stars"), (5, "5 Stars"))
class Article(models.Model):
    """
    Stores a single blog post entry related to  :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="article_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"Article: {self.title} | written by {self.author}"
       
            
class Event(models.Model):
    """
    Stores a single event post entry related to  :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="event_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"Event: {self.title} | Posted by {self.author}"

class Review(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`review.Post`.
    """
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="review")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING, default=1)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Review {self.body[:50]}... by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`article.Post`.
    """
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body[:50]}... by {self.author}"    
