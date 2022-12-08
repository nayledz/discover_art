from django.contrib import admin
from django.contrib.admin import ModelAdmin

from discover_art.art_contact.models import ArtContact


@admin.register(ArtContact)
class ContactFormAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    ordering = ('date_received',)
    readonly_fields = ('date_received',)
