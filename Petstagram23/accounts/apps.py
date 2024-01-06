from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Petstagram23.accounts'

    def ready(self):
        result = super().ready()
        import Petstagram23.accounts.signals
        return result

