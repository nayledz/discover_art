from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from discover_art.art_accounts.models import Account


UserModel = get_user_model()


class AccountDetailsForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ('user',)


class AccountEditForm(forms.ModelForm):

    class Meta:
        model = Account
        exclude = ('user',)



