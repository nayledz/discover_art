from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from discover_art.art_products.forms import ProductEditForm
from discover_art.art_products.models import Product
from discover_art.core.model_mixins import LoginRequiredMixin



def index(request):
    product = Product.objects.filter()
    context = {
        'product': product,
    }
    return render(request, 'index.html', context)


def about_us(request):
    return render(request, 'about.html')


def paintings_categories(request):
    product = Product.objects.filter()
    context = {
        'product': product,
    }
    return render(request, 'products.html', context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'products/product-add-page.html'
    model = Product
    fields = ('category', 'name', 'price', 'product_image', 'description', 'location', 'quantity', 'size', 'used_materials')
    success_url = reverse_lazy('my products')
    login_url = '/log-in/'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class ProductDetailsView(DetailView):
    template_name = 'products/product-details-page.html'
    context_object_name = 'product'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        product = context['product']

        product_owner = product.user == self.request.user
        context['product_owner'] = product_owner

        return context


class ProductEditView(LoginRequiredMixin, UpdateView):
    template_name = 'products/product-edit-page.html'
    form_class = ProductEditForm
    model = Product

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("product details", kwargs={"pk": pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'products/product-delete-page.html'
    model = Product
    success_url = reverse_lazy('my products')


class SearchResultsView(ListView):
    model = Product
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            query = ''
        object_list = Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


@login_required(login_url='/log-in/')
def my_products_list(request):
    products = Product.objects.all()
    total_products = Product.objects.count()
    my_products = []
    for product in products:
        if product.user_id == request.user.id:
            my_products.append(product)

    context = {
        'products': my_products,
        'total_products': total_products,
        'my_products': len(my_products),
    }

    return render(request, 'products/my-products.html', context)

# def category_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter()
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     context = {'category': category, 'categories': categories, 'products': products}
#     return render(request, '', context)

def landscapes(request):
    products = Product.objects.all()
    landscapes_products = []
    for product in products:
        if product.category == 'landscapes':
            landscapes_products.append(product)

    context = {
        'landscapes_products': landscapes_products,
    }

    return render(request, 'products/landscapes.html', context)


def abstracts(request):
    products = Product.objects.all()
    abstracts_products = []
    for product in products:
        if product.category == 'abstracts':
            abstracts_products.append(product)

    context = {
        'abstracts_products': abstracts_products,
    }

    return render(request, 'products/abstracts.html', context)


def portraits(request):
    products = Product.objects.all()
    portraits_products = []
    for product in products:
        if product.category == 'people_and_portraits':
            portraits_products.append(product)

    context = {
        'portraits_products': portraits_products,
    }

    return render(request, 'products/portraits.html', context)


def florals(request):
    products = Product.objects.all()
    florals_products = []
    for product in products:
        if product.category == 'florals_and_plants':
            florals_products.append(product)

    context = {
        'florals_products': florals_products,
    }

    return render(request, 'products/florals.html', context)


def still_life(request):
    products = Product.objects.all()
    still_life_products = []
    for product in products:
        if product.category == 'still_life':
            still_life_products.append(product)

    context = {
        'still_life_products': still_life_products,
    }

    return render(request, 'products/still_life.html', context)


def animals(request):
    products = Product.objects.all()
    animals_products = []
    for product in products:
        if product.category == 'animals':
            animals_products.append(product)

    context = {
        'animals_products': animals_products,
    }

    return render(request, 'products/animals.html', context)


def cities(request):
    products = Product.objects.all()
    cities_products = []
    for product in products:
        if product.category == 'architecture_and_cities':
            cities_products.append(product)

    context = {
        'cities_products': cities_products,
    }

    return render(request, 'products/cities.html', context)