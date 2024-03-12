from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from .models import Story

from .forms import CommentForm



# Views for Article model
def article_detail(request, slug):
    article = get_object_or_404(Stories, slug=slug)
    return render(request, 'articles_detail.html', {'articles': articles})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})

@login_required
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_form.html', {'form': form})

@login_required
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        article.delete()
        return redirect('home')
    return render(request, 'article_confirm_delete.html', {'article': article})

def story_list(request):
    stories = Story.objects.all()
    return render(request, 'stories/story_list.html', {'stories': stories})