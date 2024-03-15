from django.shortcuts import HttpResponse, redirect
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, blank=True, null=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    website_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)

    # avatar selection or upload own pic
    def set_avatar(self, avatar_url):
        self.profile_picture = avatar_url
        self.save()

    def __str__(self):
        return str(self.user)

def profile_picture_upload(request):
    if request.method == 'POST':
        # Assuming the form field for the uploaded image is named 'profile_picture'
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            request.user.profile.profile_picture = profile_picture
            request.user.profile.save()
            return HttpResponse("Profile picture uploaded successfully!")
    # Handle GET request or invalid form submission
    return HttpResponse("Profile picture upload failed!")  # You may want to render a template instead


class Story(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # Add a slug field
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00) 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Auto-generate slug from title
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    GENRE_CHOICES = [
        ('supernatural', 'Supernatural Horror'),
        ('psychological', 'Psychological Horror'),
        ('slasher', 'Slasher'),
        ('zombie', 'Zombie Apocalypse'),
        ('found_footage', 'Found Footage'),
        ('monster', 'Monster'),
        ('survival', 'Survival Horror'),
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.story.title}"

RATING = ((1, "1 Star"), (2, "2 Stars"), (3, "3 Stars"), (4, "4 Stars"), (5, "5 Stars"))

class Review(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING, default=1)

    def __str__(self):
        return f"Review by {self.author} on {self.story.title}"
