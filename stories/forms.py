from django import forms
from .models import Comment, Review
from .models import Story

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

class ProfileForm(forms.Form):
    picture = forms.ImageField(label='Upload Profile Picture', required=False)

    def clean(self):
        cleaned_data = super().clean()
        picture = cleaned_data.get('picture')
        if picture:
            # Handle picture upload logic here (using Cloudinary)
            pass
        return cleaned_data
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # Remove instance argument
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)  # Remove instance argument

    return render(request, 'edit_profile.html', {'form': form})
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