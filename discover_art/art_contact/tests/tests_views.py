
from django.test import TestCase
from django.urls import reverse


class TestsURLs(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('contact us'))
        self.assertEqual(response.status_code, 200)