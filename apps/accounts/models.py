"""Contains the accounts app models."""
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Define the users model."""
    id = models.UUIDField(
        primary_key=True,
        verbose_name='id',
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    email = models.EmailField(
        _('email address'),
        blank=False,
        unique=True
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
