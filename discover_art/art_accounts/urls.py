from django.urls import path, include

from discover_art.art_accounts.views import AccountDeleteView, profile_edit_view, profile_details

urlpatterns = (
    path('profile/<int:pk>/', include([
        path('details/', profile_details, name='details account'),
        path('edit/', profile_edit_view, name='edit account'),
        path('delete/', AccountDeleteView.as_view(), name='delete account'),
    ])),
)