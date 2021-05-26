from django.views.generic.list import BaseListView

from yoda.views.mixins import MultipleObjectJsonResponseMixin


# TODO: implement query parameters.
class APIListView(MultipleObjectJsonResponseMixin, BaseListView):
    paginate_by = 100
    ordering = ["-id"]
