from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CommentForm, HorrorGenreForm, ReviewForm  # Import forms instead of models
from .models import Story 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def post_list(request):
    queryset = Story.objects.all()  # Change the queryset to fetch all stories
    return render(request, 'stories/stories.html', {'object_list': queryset})

def post_detail(request, slug):
    post = get_object_or_404(Story, slug=slug)
    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.story = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return redirect('stories_detail', slug=post.slug)

    comment_form = CommentForm()
    review_form = ReviewForm()
    genre_form = HorrorGenreForm()

    return render(
        request,
        "stories/stories_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "review_form": review_form,
            "genre_form": genre_form
        },
    )

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
        return redirect('profile')  # Redirect to the user's profile page
    else:
        return render(request, 'set_avatar.html')

@login_required
def profile_view(request):
    # Retrieve user's profile
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})