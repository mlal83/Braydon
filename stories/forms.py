from django import forms
from .models import Story, Comment, Review, Profile


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
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']

    picture = forms.ImageField(label='Upload Profile Picture', required=False)
    avatar = forms.ChoiceField(label='Select Avatar', choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically populate choices for avatar field
        self.fields['avatar'].choices = [(avatar.url, avatar.url) for avatar in Avatar.objects.all()]

    def clean(self):
        cleaned_data = super().clean()
        picture = cleaned_data.get('picture')
        avatar = cleaned_data.get('avatar')
        
        if not picture and not avatar:
            raise forms.ValidationError('Please upload a photo or select an avatar.')

        return cleaned_data

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content']     
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)