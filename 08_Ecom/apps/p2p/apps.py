from django.apps import AppConfig


class P2PConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.p2p"
    label = "p2p"

    def ready(self) -> None:
        pass