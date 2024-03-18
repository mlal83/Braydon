from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .forms import CommentForm, HorrorGenreForm, ReviewForm
from .models import Story, Profile  
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm
from .forms import StoryForm
from django.views.generic import ListView



class StoryList(ListView):
    """
    Display a list of :model:`story.Story`

    **Context**

    ``story``
        An instance of :model:`story.Story`.

    **Template:**

    :template:`stories.list.html`
    """
    queryset = Story.objects.all()
    template_name = "stories.list.html"
    context_object_name = "stories.list"



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

@login_required
def set_avatar(request):
    if request.method == 'POST':
        try:
            avatar_file = request.FILES['avatar_file']
            profile = request.user.profile
            profile.profile_picture = avatar_file
            profile.save()
            messages.success(request, 'Avatar updated successfully.')
        except (KeyError, ObjectDoesNotExist):
            messages.error(request, 'Failed to update avatar. Please try again.')
        return redirect('profile')
    else:
        return render(request, 'set_avatar.html')


def profile_picture_upload(request):
    # Your view logic for profile picture upload
    return HttpResponse("Profile picture uploaded successfully!")

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
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
                profile.picture = request.FILES['picture']  # Assuming 'picture' is the name of the field in the form
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'upload_profile_picture.html', {'form': form})

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
    return render(request, 'submit_story.html', {'form': form})