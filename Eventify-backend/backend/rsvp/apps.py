from django.apps import AppConfig

class RsvpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rsvp'
    
    def ready(self):
        import rsvp.signals
