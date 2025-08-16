from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=15,
        label="Nombre de usuario",
        help_text="Obligatorio. 15 caracteres o menos. Letras, dígitos y @/./+/-/_ únicamente."
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")