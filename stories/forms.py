from django import forms

class HorrorGenreForm(forms.Form):
    GENRE_CHOICES = [
        ('supernatural', 'Supernatural Horror'),
        ('psychological', 'Psychological Horror'),
        ('slasher', 'Slasher'),
        ('zombie', 'Zombie Apocalypse'),
        ('found_footage', 'Found Footage'),
        ('monster', 'Monster'),
        ('survival', 'Survival Horror'),
    ]

    genre = forms.ChoiceField(choices=GENRE_CHOICES)

# Move the model imports below the HorrorGenreForm class
from .models import Comment, Review

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)
