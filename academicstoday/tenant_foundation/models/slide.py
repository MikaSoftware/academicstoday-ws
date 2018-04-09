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


class SlideManager(models.Manager):
    def delete_all(self):
        items = Slide.objects.all()
        for item in items.all():
            item.delete()


class Slide(models.Model):
    """
    Class represents a lecture inside a course.
    """
    class Meta:
        app_label = 'tenant_foundation'
        db_table = 'at_slides'
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')

    objects = SlideManager()

    lecture = models.ForeignKey(
        "Lecture",
        help_text=_('The lecture this slide belongs to.'),
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_lecture_related",
        on_delete=models.CASCADE
    )

    title = models.CharField(
        _("Title"),
        help_text=_('The title of this slide.'),
        max_length=63,
        db_index=True,
    )
    description = models.TextField(
        _("Description"),
        help_text=_('The slide description.'),
        null=True,
        blank=True
    )


    # These fields are used to track time/date of this application.
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
    last_modified_at = models.DateTimeField(auto_now=True, db_index=True,)

    def __str__(self):
        return str(self.pk)
