from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(help_text="Email address")
    first_name = forms.CharField(max_length=30, help_text="First name")
    last_name = forms.CharField(max_length=30, help_text="Last name")
    profile_photo_url = forms.URLField(required=False, help_text="Host your image on a service like https://postimages.org/ and paste the URL here.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'profile_photo_url')
        help_texts = {
            'username': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="User Name")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Password")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_photo_url')
