from django import forms
from .models import CustomerOrder

class TShirtOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['category', 'size', 'custom_image', 'description', 'delivery_address', 'artist']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your design idea...'}),
        }

class AccessoriesOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['category', 'custom_image', 'description', 'delivery_address', 'artist']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your design idea...'}),
        }

class CanvasOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['category', 'size', 'frame_option', 'custom_image', 'description', 'delivery_address', 'artist']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your design idea...'}),
        }
