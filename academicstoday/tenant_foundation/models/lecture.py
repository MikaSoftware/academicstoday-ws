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


class LectureManager(models.Manager):
    def delete_all(self):
        items = Lecture.objects.all()
        for item in items.all():
            item.delete()


class Lecture(models.Model):
    """
    Class represents a lecture inside a course. Some academies call this a "chapter".
    """
    class Meta:
        app_label = 'tenant_foundation'
        db_table = 'at_lectures'
        verbose_name = _('Lecture')
        verbose_name_plural = _('Lectures')

    objects = LectureManager()

    course = models.ForeignKey(
        "Course",
        help_text=_('The course this lecture belongs to.'),
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_course_related",
        on_delete=models.CASCADE
    )

    title = models.CharField(
        _("Title"),
        help_text=_('The title of this course.'),
        max_length=63,
        db_index=True,
        default=''
    )
    description = models.TextField(
        _("Description"),
        help_text=_('The description of this lecture.'),
        default='',
        null=True,
        blank=True
    )
    # lecture_num = models.PositiveSmallIntegerField(
    #     _("Lecture Number"),
    #     help_text=_('The lecture number this is.'),
    #     validators=[MinValueValidator(1)],
    #     default=1
    #     blank=True,
    #     db_index=True,
    # )
    # week_num = models.PositiveSmallIntegerField(
    #     _("Week Number"),
    #     help_text=_('The week number this lecture is on..'),
    #     validators=[MinValueValidator(1)],
    #     default=1
    #     blank=True
    # )


    # These fields are used to track time/date of this application.
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
    last_modified_at = models.DateTimeField(auto_now=True, db_index=True,)

    def __str__(self):
        return str(self.pk)
