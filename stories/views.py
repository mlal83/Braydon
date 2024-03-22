from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .forms import CommentForm, HorrorGenreForm, ReviewForm
from .models import Story, Profile  
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, StoryForm, forms
from django.views.generic import ListView


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
    This StoryList view Lists the storys in a more userfriendly way were the user
    can click in to the story car which expands to the story 
    """
    model = Story
    template_name = "stories/stories.html"
    context_object_name = "stories"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the genre form
        context['genre_form'] = HorrorGenreForm()
        return context

def select_genre(request):

    """
    when the user submits a story, they are asked to select the genre from the drop down
    bar which showcases the story type.
    """  
    if request.method == 'POST':
        genre_form = HorrorGenreForm(request.POST)
        if genre_form.is_valid():
            pass  # Handle the valid form.
    else:
        genre_form = HorrorGenreForm()
    
    context = {
        'genre_form': genre_form,
    }
    return render(request, 'stories.html', context)

    
class StoryDetailView(DetailView):
    """
    The storyDetail view retrieves the story, query the user, counts the number of comments and 
    displays there reviews and provides the option to rate the story 
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
            context['profile_picture_upload'] = user_profile.profile_picture_upload
            
        context['comments'] = story.comments.all().order_by("-created_at")
        context['comment_count'] = story.comments.filter(approved=True).count()
        context['comment_form'] = CommentForm()
        context['review_form'] = ReviewForm()
        context['genre_form'] = HorrorGenreForm()
        return context


def comment_edit(request, slug, comment_id):
    """
    The comment edit view attempts to update data and sends a message that the comment
    is updated successfully
    """ 
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment updated successfully.')
            return redirect('stories_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'stories/stories_detail.html', {'form': form})

def comment_delete(request, slug, comment_id):
    """
    The comment delete view deletes data and also provides a success message that comment 
    successfully deleted
    """ 
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    return redirect('stories_detail', slug=slug)


def edit_profile_form(request):

    """
    The edit profile view attempts to update data on the user profile
    """ 
    if request.method =='POST':
        form=profile_view (request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save ()

    else:
        form = ProfileForm(instance=request.user.profile)
        (request, 'profile.html', {'form': form})

    
@login_required

    """
    This view manages the user profile, whether its present or creating a new user
    """ 
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    stories = Story.objects.filter(author=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'profile': profile, 'stories': stories, 'form': form })
    

@login_required

    """
    The submit story view handles the submission of the story
    """ 
def submit_story(request):
    if request.method == 'POST':
       
        story_form = StoryForm(request.POST, request.FILES)
        comment_form = CommentForm(request.POST)

       
        if story_form.is_valid():
            story = story_form.save(commit=False)
            story.author = request.user
            story.save()

            # If story form is valid, validate and save comment form
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.story = story
                comment.save()
                messages.success(request, 'Story and comment submitted successfully.')
                return redirect('home')
            else:
                # If comment form is invalid, display error message
                messages.error(request, 'Comment form submission failed. Please check the errors below.')
        else:
            # If story form is invalid, display error message
            messages.error(request, 'Story form submission failed. Please check the errors below.')
    else:
        # If request method is not POST, create empty forms
        story_form = StoryForm()
        comment_form = CommentForm()
        genre_form = HorrorGenreForm()

    # Pass the forms to the template
    return render(request, 'stories/stories_detail.html', {'story_form': story_form, 'comment_form': comment_form  'genre_form':  genre_form})

def view_profile (request, profile_id):
 """
 This view retrieves user profiles but looking up profile ID
 """ 
    profile=get_object_or_404(UserProfile, id=profile_id) 
    return render (request, 'profile.html', {'profile': profile})

