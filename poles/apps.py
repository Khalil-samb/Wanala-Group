from django.apps import AppConfig
from django.db.models.signals import post_migrate


class PolesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'poles'

    def ready(self):
        from .views import ensure_default_poles

        def create_default_poles(sender, **kwargs):
            ensure_default_poles()

        post_migrate.connect(create_default_poles, sender=self)
