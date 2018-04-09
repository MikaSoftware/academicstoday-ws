# -*- coding: utf-8 -*-
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.utils.html import escape
from django.db.models import Q
from django.utils import timezone
from shared_foundation.models import SharedUser
from shared_foundation.constants import AT_APP_DEFAULT_MONEY_CURRENCY


class SlideOrderManager(models.Manager):
    def delete_all(self):
        items = SlideOrder.objects.all()
        for item in items.all():
            item.delete()


class SlideOrder(models.Model):
    """
    """
    class Meta:
        app_label = 'tenant_foundation'
        db_table = 'at_slide_orders'
        verbose_name = _('Slide Order')
        verbose_name_plural = _('Slide Orders')
        ordering = ['order_num',]

    objects = SlideOrderManager()

    lecture = models.ForeignKey(
        "Lecture",
        help_text=_('The lecture this belongs to.'),
        related_name="%(app_label)s_%(class)s_lecture_related",
        on_delete=models.CASCADE
    )
    slide = models.ForeignKey(
        "Slide",
        help_text=_('The slide this belongs to.'),
        related_name="%(app_label)s_%(class)s_lecture_related",
        on_delete=models.CASCADE
    )
    order_num = models.PositiveSmallIntegerField(
        _("Order Number"),
        help_text=_('The order number this slide belongs to in the lecture.'),
        validators=[MinValueValidator(1)],
    )


    def __str__(self):
        return str(self.pk)
