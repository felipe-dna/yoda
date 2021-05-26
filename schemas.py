from typing import Optional

from pydantic import BaseModel
from django.db.models import QuerySet
from django.core.paginator import Paginator, Page


class ListResponseSchema(BaseModel):
    paginator: Optional[Paginator] = None
    page_obj: Page
    is_paginated: bool
    object_list: QuerySet

    class Config:
        arbitrary_types_allowed = True
