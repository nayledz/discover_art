from django.urls import path, include

from discover_art.art_products.views import index, ProductCreateView, ProductDetailsView, \
    ProductDeleteView, ProductEditView, SearchResultsView, my_products_list, about_us, paintings_categories, \
    abstracts, portraits, florals, still_life, animals, cities, landscapes

urlpatterns = (
    path('', index, name='index'),
    path('categories/', paintings_categories, name='categories'),
    path('landscapes/', landscapes, name='landscapes'),
    path('abstracts/', abstracts, name='abstracts'),
    path('portraits/', portraits, name='portraits'),
    path('florals/', florals, name='florals'),
    path('still-life/', still_life, name='still life'),
    path('animals/', animals, name='animals'),
    path('architecture/', cities, name='cities'),
    path('about/', about_us, name='about us'),
    path('my-products/', my_products_list, name='my products'),
    path("search/", SearchResultsView.as_view(), name="search results"),
    path('product/', include([
        path('create/', ProductCreateView.as_view(), name='product create'),
        path('details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
        path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product delete'),
        path('edit/<int:pk>/', ProductEditView.as_view(), name='product edit'),
    ])),
)

