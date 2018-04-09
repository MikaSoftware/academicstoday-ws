# -*- coding: utf-8 -*-
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from datetime import timedelta
from django.db import models
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.utils.html import escape
from django.db.models import Q
from django.utils import timezone
from shared_foundation.models import SharedUser
from shared_foundation.constants import AT_APP_DEFAULT_MONEY_CURRENCY


class CourseManager(models.Manager):
    def delete_all(self):
        items = Course.objects.all()
        for item in items.all():
            item.delete()


class Course(models.Model):
    """
    Class represents a course in a educational program.
    """
    class Meta:
        app_label = 'tenant_foundation'
        db_table = 'at_courses'
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    objects = CourseManager()

    title = models.CharField(
        _("Title"),
        help_text=_('The title of this course.'),
        max_length=63,
        db_index=True,
    )
    sub_title = models.CharField(
        _("Sub-Title"),
        help_text=_('The sub-title of this course.'),
        max_length=127,
        blank=True,
        null=True,
    )
    category_text = models.CharField(
        _("Category Text"),
        help_text=_('The category text of this course.'),
        max_length=127,
        db_index=True,
    )
    description = models.TextField(
        _("Description"),
        help_text=_('The course description.'),
        null=True,
        blank=True
    )
    status = models.PositiveSmallIntegerField(
        _("Description"),
        blank=True,
        default=0
    )
    # image = models.ImageField(upload_to='uploads', null=True, blank=True)
    # students = models.ManyToManyField(Student)
    # teacher = models.ForeignKey(Teacher)
    purchase_fee = MoneyField(
        _("Purchase Fee"),
        help_text=_('The purchase fee that the student will be charged to enroll in this course.'),
        max_digits=10,
        decimal_places=2,
        default_currency=AT_APP_DEFAULT_MONEY_CURRENCY,
        default=Money(0,AT_APP_DEFAULT_MONEY_CURRENCY),
        blank=True,
    )

    lectures = models.ManyToManyField(
        'Lecture',
        through='LectureOrder',
        related_name='%(app_label)s_%(class)s_course_related'
    )

    # These fields are used to track time/date of this application.
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,)
    last_modified_at = models.DateTimeField(auto_now=True, db_index=True,)

    def __str__(self):
        return str(self.pk)
