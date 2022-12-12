from django.contrib import auth
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.test import TestCase, Client
from django.urls import reverse

from discover_art.art_products.models import Product

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






