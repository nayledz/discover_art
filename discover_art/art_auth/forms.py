from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError



UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email*'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your password*'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repeat your password*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class LogInForm(AuthenticationForm):
    user = None

    def clean_password(self):
        super().clean()
        self.user = authenticate(
            email=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError('Incorrect email and/or password!')

    def save(self):
        return self.user