from django import forms
from .models import Story, Comment, Review, Profile

GENRE_CHOICES = [
    ('supernatural', 'Supernatural Horror'),
    ('psychological', 'Psychological Horror'),
    ('slasher', 'Slasher'),
    ('zombie', 'Zombie Apocalypse'),
    ('found_footage', 'Found Footage'),
    ('monster', 'Monster'),
    ('survival', 'Survival Horror'),
]

# genre = forms.ChoiceField(choices=GENRE_CHOICES)
class HorrorGenreForm(forms.Form):
    genre = forms.ChoiceField(label='Select Genre', choices=GENRE_CHOICES)
        

class ProfileForm(forms.ModelForm):
    profile_picture_upload = forms.ImageField(label='Upload Profile Picture', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].required = False

    def clean(self):
        cleaned_data = super().clean()
        picture = cleaned_data.get('profile_picture_upload')

        if not picture:
            raise forms.ValidationError('Please upload a picture')

        return cleaned_data

    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture_upload', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content', 'genre']     


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)
