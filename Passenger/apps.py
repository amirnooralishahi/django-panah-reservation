from django.apps import AppConfig


class UserConfig ( AppConfig):
  name='Passenger'
  def ready(self):
    import Passenger.signals