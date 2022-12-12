from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user('some@email.com', 'Some1996')

    def testLogin(self):
        self.client.login(email='some@email.com', password='Some1996')
        response = self.client.get(reverse('log in'))
        self.assertEqual(response.status_code, 200)


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.email = 'some@email.com'
        self.password1 = 'Some1996'
        self.password2 = 'Some1996'

    def test_signup_page_url(self):
        response = self.client.get("/sign-up/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/register-page.html')


    def test_signup_form(self):
        response = self.client.post(reverse('sign up'), data={
            'email': self.email,
            'password1': self.password1,
            'password2': self.password2
        })
        self.assertEqual(response.status_code, 302)

        users = UserModel.objects.all()
        self.assertEqual(users.count(), 1)