from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Story

def story_list(request):
    stories = Story.objects.all()
    return render(request, 'stories/story_list.html', {'stories': stories})

def story_detail(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    return render(request, 'stories/story_detail.html', {'story': story})