from django.urls import path

from discover_art.art_auth import views

urlpatterns = (
    path('sign-up/', views.UserRegisterView.as_view(), name='sign up'),
    path('log-in/', views.UserLoginView.as_view(), name='log in'),
    path('log-out/', views.UserLogoutView.as_view(), name='log out'),
)