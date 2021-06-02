from django.apps import AppConfig
from django.conf import settings


class YodaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yoda'

    def __init__(self, app_name, app_value):
        super().__init__(app_name, app_value)
        settings.CSRF_FAILURE_VIEW = 'yoda.views.errors.missing_csrf_token_error_view'