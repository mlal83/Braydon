from django.contrib import admin
from .models import Story, Comment, Review

# Register your models here.
admin.site.register(Story)
admin.site.register(Comment)
admin.site.register(Review)