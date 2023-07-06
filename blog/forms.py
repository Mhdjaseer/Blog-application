from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomAdminLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email", 
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        UserModel = get_user_model()
        try:
            UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            raise forms.ValidationError("Invalid email or password.")
        return username


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
       