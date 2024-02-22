from django.apps import AppConfig


class SocNetworkConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "soc_network"
    verbose_name = 'Soc Network'

    def ready(self):
        import soc_network.signals