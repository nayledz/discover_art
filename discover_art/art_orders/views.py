from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from discover_art.art_orders.forms import OrderForm
from discover_art.art_orders.models import Order
from discover_art.art_products.models import Product
from discover_art.core.model_mixins import LoginRequiredMixin


class OrderProduct(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order message')
    template_name = 'orders/order_product.html'
    login_url = '/log-in/'

    def form_valid(self, form):
        order = form.save(commit=False)
        product = Product.objects.get(pk=self.kwargs['pk'])
        order.user = self.request.user
        order.product_id = product.id
        order.ordered_date = datetime.now()

        return super().form_valid(form)


@login_required(login_url='/log-in/')
def order_message(request):
    return render(request, 'orders/order_message.html')


@login_required(login_url='/log-in/')
def order_requests_notifications(request):

    orders = Order.objects.all()
    products = Product.objects.all()

    ordered_paintings = []
    order_requests = []

    for order in orders:
        for product in products:
            if order.product_id == product.id:
                product = Product.objects.get(pk=order.product_id)
                if product.user_id == request.user.id:
                    ordered_paintings.append(product)
                    order_requests.append(order)

    context = {
        'ordered_paintings': ordered_paintings,
        'order_requests': order_requests,
    }

    return render(request, 'orders/orders_requests.html', context)