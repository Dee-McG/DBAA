from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        """
        Override django AppConfig 'ready()' method to 
        create/update a profile for each user
        """
        import profiles.signals
