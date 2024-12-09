from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Artist
from .forms import CustomUserChangeForm, CustomUserForm

# Get the user model
UserModel = get_user_model()


# Custom User Admin
@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    # Use custom forms for add and change
    form = CustomUserChangeForm
    add_form = CustomUserForm

    # Display fields in the list view
    list_display = ('email', 'username', 'is_staff', 'is_active', 'last_login')

    # Add custom fieldsets for creating a user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

    # Define fieldsets to be displayed in the edit user form
    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
        ('Profile', {'fields': ('profile',)}),  # Link the Profile model here
    )

    # Add a read-only display for `profile` in user list
    readonly_fields = ('profile',)

    # Define the link for creating a profile when a new user is created
    def save_model(self, request, obj, form, change):
        if not obj.profile:
            obj.profile = Profile.objects.create(user=obj)
        obj.save()


# Admin for Profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Display these fields in the Profile list view
    list_display = ('user', 'first_name', 'last_name', 'age')

    # Enable editing these fields in the admin form
    fields = ('user', 'first_name', 'last_name', 'age')

    # Ensure user cannot be selected twice in the profile (One-to-One relationship)
    def save_model(self, request, obj, form, change):
        # Ensure a Profile is only created once per user
        if not obj.user.profile:
            obj.save()
        else:
            super().save_model(request, obj, form, change)


# Admin for Artist model
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'bio')  # Display artist fields
    search_fields = ('name', 'bio')  # Allow search by name and bio
    ordering = ('name',)  # Ordering by artist name

    # Add filters for experience range
    list_filter = ('experience',)

    # Custom form if needed
    # form = ArtistForm  # Uncomment and define if you have a custom form for the Artist model
