from django.views.generic.detail import BaseDetailView

from yoda.views.mixins import JsonResponseMixin


class APIItemView(JsonResponseMixin, BaseDetailView):
    ...
