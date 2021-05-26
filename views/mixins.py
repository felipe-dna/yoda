from typing import Type, Dict, Any

from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from pydantic import BaseModel

from yoda.schemas import ListResponseSchema


class JsonResponseMixin:
    """A mixin that can be used to return an json response."""
    content_type = "application/json"
    response_class = JsonResponse
    response_schema: Type[BaseModel] = None
    context_object_name: str = "object"

    def render_to_response(self, context: Dict[str, Any]) -> JsonResponse:
        if self.response_schema is None:
            raise ImproperlyConfigured("Missing response_schema parameter.")

        response = self.response_schema.from_orm(
            context[self.context_object_name]
        ).dict()

        return self.response_class(
            data=response,
            content_type=self.content_type,
        )


class MultipleObjectJsonResponseMixin(JsonResponseMixin):
    context_object_name: str = "object_list"

    def render_to_response(self, context: Dict[str, Any]) -> JsonResponse:
        context_data = ListResponseSchema(**context)

        if self.response_schema is None:
            raise ImproperlyConfigured("Missing response_schema parameter.")

        context_dict = dict()
        context_dict[self.context_object_name] = [
            context_object
            for context_object in context_data.object_list
        ]

        if context_data.is_paginated:
            context_dict["page"] = context_data.page_obj.number

            if context_data.page_obj.has_next():
                context_dict["next"] = context_data.page_obj.number + 1

            if context_data.page_obj.has_previous():
                context_dict["previous"] = context_data.page_obj.number - 1

        response = self.response_schema(**context_dict).dict(
            exclude_defaults=True)

        return self.response_class(
            data=response,
            content_type=self.content_type,
            safe=False
        )
