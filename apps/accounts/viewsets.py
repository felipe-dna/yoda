"""Contains the accounts API views."""
from datetime import datetime
from typing import Dict, Any

from rest_framework.authentication import BasicAuthentication

from knox.views import LoginView as KnoxLoginView


class LoginView(KnoxLoginView):
    """"""
    authentication_classes = [BasicAuthentication]

    async def get_context(self) -> Dict[str, Any]:
        context: Dict[str, Any] = super(LoginView, self).get_context()
        return context

    async def get_token_ttl(self) -> str:
        return super(LoginView, self).get_token_ttl()

    async def get_token_limit_per_user(self) -> str:
        return super(LoginView, self).get_token_limit_per_user()

    async def get_user_serializer_class(self) -> object:
        return super(LoginView, self).get_user_serializer_class()

    def get_expiry_datetime_format(self) -> str:
        return super(LoginView, self).get_expiry_datetime_format()

    def format_expiry_datetime(self, expiry: str) -> datetime:
        return super(LoginView, self).format_expiry_datetime(expiry)

    def get_post_response_data(self, request, token, instance):
        return super(LoginView, self).get_post_response_data(request, token, instance)

    def post(self, request, format=None):
        return super(LoginView, self).post(request, format)

    def as_view(cls, **initkwargs):
        return super().as_view(**initkwargs)
