from django.urls import path

from discover_art.art_orders import views
from discover_art.art_orders.views import order_message, order_requests_notifications

urlpatterns = (
    path('product/order/<int:pk>', views.OrderProduct.as_view(), name='order product'),
    path('product/order/order-message', order_message, name='order message'),
    path('orders-requests', order_requests_notifications, name='orders requests'),


)