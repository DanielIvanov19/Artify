from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# class ArtistProfileForm(forms.ModelForm):
#     class Meta:
#         model = ArtistProfile
#         fields = ['bio', 'specialization', 'experience', 'profile_picture']
#         widgets = {
#             'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a short bio about yourself...'}),
#         }

class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = "__all__"