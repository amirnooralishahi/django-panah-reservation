from django.apps import AppConfig

class ReservationConfig(AppConfig):
    name = 'Payment'

    def ready(self):
        import Payment.signals