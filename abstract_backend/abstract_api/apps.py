from django.apps import AppConfig


class AbstractApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abstract.api'
