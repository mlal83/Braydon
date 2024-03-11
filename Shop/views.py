from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article, Event, Comment, Review
from .forms import CommentForm, ReviewForm


# Create your views here.


class ArticleList(ListView):
    """
    Display a list of :model:`article.Article`

    **Context**

    ``article``
        An instance of :model:`article.Article`.

    **Template:**

    :template:`article/articles.html`
    """
    queryset = Article.objects.filter(status=1)
    template_name = "articles/articles.html"


class EventList(ListView):
    """
    Display a list of :model:`event.Events`

    **Context**

    ``event``
        An instance of :model:`event.Event`.

    **Template:**

    :template:`events.html`
    """
    queryset = Event.objects.filter(status=1)
    template_name = "articles/events.html"


def article_detail(request, slug):
    """
    Display an individual :model:`article.Post`.

    **Context**

    ``article``
        An instance of :model:`article.Post`.

    **Template:**

    :template:`article_detail.html`
    """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comments = article.comments.all().order_by("-created_on")
    comment_count = article.comments.filter(approved=True).count()


    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.add_message(
    request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
    )

    
    comment_form = CommentForm()

    return render(
            request,
            "articles/article_detail.html",
            {"article": article,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form}
    )


def event_detail(request, slug):
    """
    Display an individual :model:`event.Post`.

    **Context**

    ``event``
        An instance of :model:`event.Post`.

    **Template:**

    :template:`event_detail.html`
    """
    
    queryset = Event.objects.filter()
    event = get_object_or_404(queryset, slug=slug)
    reviews = event.review.all().order_by("-created_on")
    review_count = event.review.filter(approved=True).count()


    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.event = event
            review.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Review submitted and awaiting approval'
    )

    review_form = ReviewForm()

    return render(
        request,
        "articles/event_detail.html",
        {"event": event,
        "reviews": reviews,
        "review_count": review_count,
        "review_form": review_form
        },
    )


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

        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
            'Error updating comment!')

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))

def review_edit(request, slug, review_id):
    """
    Display an individual review for edit.

    **Context**

    ``article``
        An instance of :model:`article.Post`.
    ``review``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`event.reviewForm`
    """
    if request.method == "POST":

        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.event = event
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR,
            'Error updating review!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))

def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))