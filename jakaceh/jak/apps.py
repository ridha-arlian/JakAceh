from django.apps import AppConfig


class JakConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jak'

    def ready(self):
        import jak.signals