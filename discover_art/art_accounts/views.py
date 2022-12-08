from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from discover_art.art_accounts.forms import AccountEditForm, AccountDetailsForm
from discover_art.art_accounts.models import Account
from django.views import generic as views

from discover_art.core.model_mixins import LoginRequiredMixin

UserModel = get_user_model()


# class AccountDetailsView(views.DetailView):
#     template_name = 'accounts/profile-details-page.html'
#     model = UserModel

@login_required(login_url='/log-in/')
def profile_details(request, pk):
    user = UserModel.objects.get(pk=pk)
    profile = Account.objects.get(user_id=user.id)
    if request.method == "GET":
        form = AccountDetailsForm(instance=profile)
    else:
        form = AccountDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details account')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'accounts/profile-details-page.html', context)


@login_required(login_url='/log-in/')
def profile_edit_view(request, pk):
    user = UserModel.objects.get(pk=pk)
    profile = Account.objects.get(user_id=user.id)

    if request.method == 'POST':
        form = AccountEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details account', pk)
    else:
        form = AccountEditForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,

    }
    return render(request, 'accounts/profile-edit-page.html', context)


class AccountDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
