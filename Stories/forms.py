from .models import Comment
from .models import Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)