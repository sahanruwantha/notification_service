from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    def ready(self):
        print("\nServer is starting... 🎉 Welcome to Your Django Application! 🎉\n")
