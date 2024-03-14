from django.contrib import admin
from .models import Story, Comment, Review
from .models import Profile

# Register your models here.
admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Profile)

