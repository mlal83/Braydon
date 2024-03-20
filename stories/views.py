from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .forms import CommentForm, HorrorGenreForm, ReviewForm
from .models import Story, Profile  
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm
from .forms import StoryForm
from django.views.generic import ListView


def display_stories(request):
    """
    Displays all stories
    """
    stories = Story.objects.all()
    context = {
        'stories': stories
        }
    return render(request, 'stories/stories.html', context)
   

class StoryList(ListView):
    model = Story
    template_name = "stories/stories.html"
    context_object_name = "stories"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the genre form
        context['genre_form'] = HorrorGenreForm()
        return context


class StoryList(ListView):
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
    model = Story
    template_name = 'stories/stories_detail.html'
    context_object_name = 'story'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by("-created_at")
        context['comment_count'] = self.object.comments.filter(approved=True).count()
        context['comment_form'] = CommentForm()
        context['review_form'] = ReviewForm()
        context['genre_form'] = HorrorGenreForm()
        return context

##def stories_detail(request, slug):
##    story = get_object_or_404(Story, slug=slug)
##    comments = story.comments.all().order_by("-created_at")
##    comment_count = story.comments.filter(approved=True).count()

##    if request.method == "POST":
##        comment_form = CommentForm(data=request.POST)
##        if comment_form.is_valid():
##            comment = comment_form.save(commit=False)
##            comment.author = request.user
##            comment.story = story
##            comment.save()
##            messages.add_message(
##                request, messages.SUCCESS,
##                'Comment submitted and awaiting approval'
##            )
##            return redirect('stories_detail', slug=story.slug)
##    else:
##        comment_form = CommentForm()
##        review_form = ReviewForm()
##        genre_form = HorrorGenreForm()


##    return render(
##        request,
##        "stories/stories_detail.html",
##        {
##            "story": story,
##            "comments": comments,
##            "comment_count": comment_count,
##            "comment_form": comment_form,
##            "review_form": review_form,
##            "genre_form": genre_form,
##        }
##    )

def comment_edit(request, slug, comment_id):
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
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    return redirect('stories_detail', slug=slug)


def profile_picture_upload(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            request.user.profile.profile_picture = profile_picture
            request.user.profile.save()
            return HttpResponse("Profile picture uploaded successfully!")
    # Handle GET request or invalid form submission 
    return HttpResponse("Profile picture upload failed!") 



def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            picture = cleaned_data.get('picture')
            if picture:
                # Save the selected avatar as the user's profile picture
                request.user.profile.profile_picture = picture
                request.user.profile.save()
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']  
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
        stories = Story.objects.filter(author=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
        stories = [] 

    return render(request, 'profile.html', {'profile': profile, 'stories': stories})

 
@login_required
def submit_story(request):
    if request.method == 'POST':
        (request.POST, request.FILES)
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            messages.success(request, 'Story submitted successfully.')
            return redirect('home')  
        else:
            messages.error(request, 'Form submission failed. Please check the errors below.')
    else:
        form = StoryForm()
    return render(request, 'stories.html', {'form': form})