# -*- coding: utf-8 -*-
from django.db import models


class BaseModel (models.Model):

    """Base model class"""

    created_at = models.DateTimeField(
        verbose_name="criado em",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="atualizado pela última vez em",
        auto_now=True,
    )

    is_active = models.BooleanField(
        verbose_name="está ativo",
        default=True
    )

    class Meta:
        abstract = True
