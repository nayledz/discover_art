from django.contrib.auth import get_user_model
from django.test import TestCase

from discover_art.art_accounts.forms import AccountEditForm

UserModel = get_user_model()


class AccountEditFormTests(TestCase):
    def test_form_only_letters_expect_not_to_be_edited(self):
        user = UserModel(email='lili12@abv.bg', password='Lili1996')
        user.full_clean()
        user.save()

        data = {
            'first_name': 'Ivan97',
            'last_name': 'Ivanov',
            'age': 22,
        }

        form = AccountEditForm(data)
        self.assertFalse(form.is_valid())

    def test_form_only_letters_expect_to_be_edited(self):
        user = UserModel(email='lili12@abv.bg', password='Lili1996')
        user.full_clean()
        user.save()
        data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'age': 22,
        }

        form = AccountEditForm(data)
        self.assertTrue(form.is_valid())