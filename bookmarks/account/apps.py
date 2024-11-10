# from django.apps import AppConfig


# class AccountConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'account'

from django.apps import AppConfig

class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):
        # Import signals to ensure they're registered when Django starts
        import account.signals

