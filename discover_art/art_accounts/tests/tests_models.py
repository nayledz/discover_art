from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from discover_art.art_accounts.models import Account

UserModel = get_user_model()


class AccountModelTest(TestCase):
    def test_validate_only_letters_expect_exception(self):
        user = UserModel(email='lili12@abv.bg', password='Lili1996')
        user.full_clean()
        user.save()

        account = Account(
            first_name='Lili98',
            last_name='Georgieva',
            age=25,
            user=user,
        )

        try:
            account.full_clean()
            account.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)




