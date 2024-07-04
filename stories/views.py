from cloudinary.utils import cloudinary_url
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .forms import CommentForm, StoryForm, ReviewForm, ProfileForm
from .models import Story, Profile, Comment, Review
from django.contrib.auth.decorators import login_required

import os

def display_stories(request):
    """
    This view displays all the user stories
    """
    stories = Story.objects.all()
    context = {
        'stories': stories
    }
    return render(request, 'stories/stories.html', context)

class StoryList(ListView):
    """
    This StoryList view Lists the stories in a more user-friendly way where the user
    can click into the story card which expands to the story
    """
    model = Story
    template_name = "stories/stories.html"
    context_object_name = "stories"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the genre form
        context['story_form'] = StoryForm()
        return context

class StoryDetailView(DetailView):
    """
    The storyDetail view retrieves the story, queries the user, counts the number of comments and 
    displays their reviews and provides the option to rate the story 
    """
    model = Story
    template_name = 'stories/stories_detail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = self.get_object()
        user_profile = Profile.objects.filter(user=story.author).first()
        if user_profile:
            context['bio'] = user_profile.bio
            context['website_url'] = user_profile.website_url
            if user_profile.profile_picture_upload:
                context['profile_picture_url'] = cloudinary_url(user_profile.profile_picture_upload.public_id)[0]
            else:
                context['profile_picture_url'] = None

        context['comments'] = story.comments.all().order_by("-created_at")
        context['comment_count'] = story.comments.filter(approved=True).count()
        context['comment_form'] = CommentForm()
        context['review_form'] = ReviewForm()
        context['story_form'] = StoryForm()
        return context

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`article.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":

        queryset = Story.objects.filter(status=1)
        story = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.story = story
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
            'Error updating comment!')

    return HttpResponseRedirect(reverse('stories_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    View to delete a comment.
    """
    try:
        # Retrieve the story object with the specified slug and active status
        story = get_object_or_404(Story, slug=slug, status=1)
        
        # Retrieve the comment object with the specified ID
        comment = get_object_or_404(Comment, pk=comment_id)
        
        # Check if the comment author matches the current user
        if comment.author == request.user:
            comment.delete()
            messages.success(request, 'Comment deleted successfully.')
        else:
            messages.error(request, 'You can only delete your own comments.')
        
    except Story.DoesNotExist:
        # Handle case where the story with the given slug and status=1 does not exist
        messages.error(request, 'Story not found.')
        return redirect('home')  # Redirect to a meaningful page
    
    except Comment.DoesNotExist:
        # Handle case where the comment with the given ID does not exist
        messages.error(request, 'Comment not found.')

    # Redirect back to the story detail page
    return HttpResponseRedirect(reverse('stories_detail', args=[slug]))

def edit_profile_form(request):
    """
    The edit profile view attempts to update data on the user profile
    """ 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})

@login_required
def profile_view(request):
    """
    This view manages the user profile, whether its present or creating a new user
    """ 
    profile, created = Profile.objects.get_or_create(user=request.user)
    stories = Story.objects.filter(author=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'profile': profile, 'stories': stories, 'form': form})

from django.shortcuts import redirect

def submit_comment(request, story_id):
    """
    The submit comment view handles the submission of comments for a particular story
    """
    story = Story.objects.get(pk=story_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment submitted successfully.')
            # Redirect to the homepage after successful comment submission
            return redirect('home')
        else:
            messages.error(request, 'Comment form submission failed. Please check the errors below.')
    else:
        form = CommentForm()

    return render(request, 'submit_comment.html', {'form': form})

@login_required
def submit_story(request):
    """
    The submit story view handles the submission of the story
    """
    if request.method == 'POST':
        story_form = StoryForm(request.POST, request.FILES)
        if story_form.is_valid():
            story = story_form.save(commit=False)
            story.author = request.user
            story.save()
            messages.success(request, 'Story submitted successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Story form submission failed. Please check the errors below.')
    else:
        story_form = StoryForm()

    return render(request, 'stories/stories.html', {'story_form': story_form})

@login_required
def view_profile(request, profile_id):
    """
    Function to view user profile
    """
    profile = get_object_or_404(Profile, id=profile_id) 
    return render(request, 'profile.html', {'profile': profile})

@login_required #need this here too?
def delete_comment(request, pk, comment_id):
    """
    The comment delete view deletes a comment and redirects to the story detail page.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if comment.author != request.user:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('home') 
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('home', pk=pk)
        
    return redirect('stories_detail', pk=pk)
