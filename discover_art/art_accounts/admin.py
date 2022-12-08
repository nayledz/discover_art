from django.contrib import admin
from django.contrib.admin import ModelAdmin

from discover_art.art_accounts.forms import AccountEditForm
from discover_art.art_accounts.models import Account


@admin.register(Account)
class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'first_name', 'last_name',)
    readonly_fields = ('user',)
    form = AccountEditForm