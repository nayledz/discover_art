from django.test import TestCase
from django.urls import reverse


class TestsURLs(TestCase):
    def test_redirect_if_not_logged_in_orders_requests(self):
        response = self.client.get(reverse('orders requests'))
        self.assertRedirects(response, '/log-in/?next=/orders-requests')

    def test_redirect_if_not_logged_in_order_message(self):
        response = self.client.get(reverse('order message'))
        self.assertRedirects(response, '/log-in/?next=/product/order/order-message')

