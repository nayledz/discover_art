from django.contrib import auth
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

UserModel = get_user_model()

class ProductTests(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_us(self):
        response = self.client.get(reverse('about us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_categories(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    # def test_logged_in_uses_correct_template(self):
    #     login = self.client.login(email='some@email.com', password='password')
    #     user = auth.get_user(self.client)
    #     response = self.client.get(reverse('product create'))
    #
    #     # Check our user is logged in
    #     self.assertEqual(int(self.client.session['user_id']), user.pk)
    #     # Check that we got a response "success"
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Check we used correct template
    #     self.assertTemplateUsed(response, 'products/product-add-page.html')





