from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'image', 'description', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe the artwork...'}),
        }
