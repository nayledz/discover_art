from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views


from discover_art.art_auth.forms import SignUpForm, LogInForm

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    model = UserModel
    form_class = SignUpForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return response


class UserLoginView(LoginView):
    form_class = LogInForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('log in')

