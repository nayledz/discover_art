from django.apps import AppConfig


class ArtAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'discover_art.art_accounts'

    def ready(self):
        import discover_art.core.signals