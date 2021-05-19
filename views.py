from typing import Any, Dict

from django.http import JsonResponse
from django.views.generic import ListView


class JsonResponseMixin:
    """A mixin that can be used to return an json response."""
    content_type = "application/json"
    response_class = JsonResponse

    async def render_to_response(self, context: Dict[str, Any]) -> JsonResponse:
        return self.response_class(
            data=context,
            content_type=self.content_type
        )


class MultipleObjectJsonResponseMixin():
    ...


class ApiListView(ListView):
    ...

