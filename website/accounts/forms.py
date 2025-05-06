from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Required. Enter valid email address."
    )
    first_name = forms.CharField(
        max_length=150, required=True, help_text="Required. 150 characters or fewer."
    )
    last_name = forms.CharField(
        max_length=150, help_text="Optional. 150 characters or fewer."
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
