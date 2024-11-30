from django import forms
from .models import ArtistProfile

class ArtistProfileForm(forms.ModelForm):
    class Meta:
        model = ArtistProfile
        fields = ['bio', 'specialization', 'experience', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a short bio about yourself...'}),
        }
