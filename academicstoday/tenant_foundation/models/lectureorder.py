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


class LectureOrderManager(models.Manager):
    def delete_all(self):
        items = Lecture.objects.all()
        for item in items.all():
            item.delete()


class LectureOrder(models.Model):
    """
    Class represents a lecture inside a course. Some academies call this a "chapter".
    """
    class Meta:
        app_label = 'tenant_foundation'
        db_table = 'at_lecture_orders'
        verbose_name = _('Lecture Order')
        verbose_name_plural = _('Lecture Orders')
        ordering = ['week_num', 'lecture_num',]

    objects = LectureOrderManager()

    course = models.ForeignKey(
        "Course",
        help_text=_('The course this lecture belongs to.'),
        related_name="%(app_label)s_%(class)s_course_related",
        on_delete=models.CASCADE
    )
    lecture = models.ForeignKey(
        "Lecture",
        help_text=_('The lecture this belongs to.'),
        related_name="%(app_label)s_%(class)s_lecture_related",
        on_delete=models.CASCADE
    )
    lecture_num = models.PositiveSmallIntegerField(
        _("Lecture Number"),
        help_text=_('The lecture number this is.'),
        validators=[MinValueValidator(1)],
        db_index=True,
    )
    week_num = models.PositiveSmallIntegerField(
        _("Week Number"),
        help_text=_('The week number this lecture is on.'),
        validators=[MinValueValidator(1)],
        blank=True,
        default=1
    )

    def __str__(self):
        return str(self.pk)
