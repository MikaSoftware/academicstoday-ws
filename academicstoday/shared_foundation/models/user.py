from __future__ import unicode_literals
from datetime import date, datetime, timedelta
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.gis.db.models import PointField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from starterkit.utils import (
    get_random_string,
    generate_hash
)
from shared_foundation import constants



def get_expiry_date(days=2):
    """Returns the current date plus paramter number of days."""
    return timezone.now() + timedelta(days=days)


class SharedUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class SharedUser(AbstractBaseUser, PermissionsMixin):
    #
    # PERSON FIELDS - http://schema.org/Person
    #
    first_name = models.CharField(
        _("First Name"),
        max_length=63,
        help_text=_('The users given name.'),
        blank=True,
        null=True,
        db_index=True,
    )
    middle_name = models.CharField(
        _("Middle Name"),
        max_length=63,
        help_text=_('The users middle name.'),
        blank=True,
        null=True,
        db_index=True,
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=63,
        help_text=_('The users last name.'),
        blank=True,
        null=True,
        db_index=True,
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birthdate = models.DateField(
        _('Birthdate'),
        help_text=_('The users birthdate.'),
        blank=True,
        null=True
    )
    join_date = models.DateTimeField(
        _("Join Date"),
        help_text=_('The date the customer joined this organization.'),
        null=True,
        blank=True,
    )
    nationality = models.CharField(
        _("Nationality"),
        max_length=63,
        help_text=_('Nationality of the person.'),
        blank=True,
        null=True,
    )
    gender = models.CharField(
        _("Gender"),
        max_length=63,
        help_text=_('Gender of the person. While Male and Female may be used, text strings are also acceptable for people who do not identify as a binary gender.'),
        blank=True,
        null=True,
    )
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)

    #
    # SYSTEM FIELD
    #

    is_active = models.BooleanField(_('active'), default=True)
    was_email_activated = models.BooleanField(
        _("Was Email Activated"),
        help_text=_('Was the email address verified as an existing address?'),
        default=False,
        blank=True
    )
    last_modified = models.DateTimeField(auto_now=True, db_index=True,)
    salt = models.CharField( #DEVELOPERS NOTE: Used for cryptographic signatures.
        _("Salt"),
        max_length=127,
        help_text=_('The unique salt value me with this object.'),
        default=generate_hash,
        unique=True,
        blank=True,
        null=True
    )
    type_of = models.PositiveSmallIntegerField(
        _("Type of"),
        help_text=_('The type of user this is. Value represents ID of user type.'),
        default=0,
        blank=True,
        db_index=True,
    )
    is_ok_to_email = models.BooleanField(
        _("Is OK to email"),
        help_text=_('Indicates whether customer allows being reached by email'),
        default=True,
        blank=True
    )
    is_ok_to_text = models.BooleanField(
        _("Is OK to text"),
        help_text=_('Indicates whether customer allows being reached by text.'),
        default=True,
        blank=True
    )

    #
    # PASSWORD RESET FIELDS
    #

    pr_access_code = models.CharField(
        _("Password Reset Access Code"),
        max_length=127,
        help_text=_('The access code to enter the password reset page to be granted access to restart your password.'),
        blank=True,
        default=generate_hash,
    )
    pr_expiry_date = models.DateTimeField(
        _('Password Reset Access Code Expiry Date'),
        help_text=_('The date where the access code expires and no longer works.'),
        blank=True,
        default=get_expiry_date,
    )

    #
    # CONTACT POINT FIELDS - http://schema.org/ContactPoint
    #
    area_served = models.CharField(
        _("Area Served"),
        max_length=127,
        help_text=_('The geographic area where a service or offered item is provided.'),
        blank=True,
        null=True,
    )
    available_language = models.CharField(
        _("Available Language"),
        max_length=127,
        help_text=_('A language someone may use with or at the item, service or place. Please use one of the language codes from the <a href="https://tools.ietf.org/html/bcp47">IETF BCP 47 standard</a>.'),
        null=True,
        blank=True,
    )
    contact_type = models.CharField(
        _("Contact Type"),
        max_length=127,
        help_text=_('A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.'),
        blank=True,
        null=True,
    )
    email = models.EmailField( # THIS FIELD IS REQUIRED.
        _("Email"),
        help_text=_('Email address.'),
        db_index=True
    )
    fax_number = PhoneNumberField(
        _("Fax Number"),
        help_text=_('The fax number.'),
        blank=True,
        null=True
    )
    telephone = PhoneNumberField(
        _("Telephone"),
        help_text=_('The telephone number.'),
        blank=True,
        null=True,
        db_index=True
    )
    telephone_extension = models.CharField(
        _("Telephone Extension"),
        max_length=31,
        help_text=_('The telephone number.'),
        blank=True,
        null=True,
    )
    mobile = PhoneNumberField( # Not standard in Schema.org
        _("Mobile"),
        help_text=_('The mobile telephone number.'),
        blank=True,
        null=True,
        db_index=True,
    )

    #
    # GEO-COORDINATE FIELDS - http://schema.org/GeoCoordinates
    #
    elevation = models.FloatField(
        _("Elevation"),
        help_text=_('The elevation of a location (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).'),
        blank=True,
        null=True
    )
    latitude = models.DecimalField(
        _("Latitude"),
        max_digits=8,
        decimal_places=3,
        help_text=_('The latitude of a location. For example 37.42242 (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).'),
        blank=True,
        null=True
    )
    longitude = models.DecimalField(
        _("Longitude"),
        max_digits=8,
        decimal_places=3,
        help_text=_('The longitude of a location. For example -122.08585 (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).'),
        blank=True,
        null=True
    )
    location = PointField(
        _("Location"),
        help_text=_('A longitude and latitude coordinates of this location.'),
        null=True,
        blank=True,
        srid=4326,
        db_index=True
    )

    #
    # POSTAL ADDRESS - http://schema.org/PostalAddress
    #
    address_country = models.CharField(
        _("Address Country"),
        max_length=127,
        help_text=_('The country. For example, USA. You can also provide the two-letter <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1 alpha-2</a> country code.'),
        blank=True,
        null=True,
    )
    address_locality = models.CharField(
        _("Address Locaility"),
        max_length=127,
        help_text=_('The locality. For example, Mountain View.'),
        blank=True,
        null=True,
    )
    address_region = models.CharField(
        _("Address Region"),
        max_length=127,
        help_text=_('The region. For example, CA.'),
        blank=True,
        null=True,
    )
    post_office_box_number = models.CharField(
        _("Post Office Box Number"),
        max_length=255,
        help_text=_('Apartment, suite, unit, building, floor, etc.'),
        blank=True,
        null=True,
    )
    postal_code = models.CharField(
        _("Postal Code"),
        max_length=127,
        help_text=_('The postal code. For example, 94043.'),
        db_index=True,
        blank=True,
        null=True,
    )
    street_address = models.CharField(
        _("Street Address"),
        max_length=255,
        help_text=_('The street address. For example, 1600 Amphitheatre Pkwy.'),
        blank=True,
        null=True,
    )
    street_address_extra = models.CharField(
        _("Street Address (Extra Line)"),
        max_length=255,
        help_text=_('Apartment, suite, unit, building, floor, etc.'),
        blank=True,
        null=True,
    )

    #
    # SYSTEM UNIQUE IDENTIFIER
    #
    identifier = models.CharField(
        _('Identifier'),
        help_text=_('The unique identifier which has email plus a tenant_id number appended to it. If no tenant_id is append then this user has not been assigned anywhere.'),
        max_length=255,
        db_index=True,
        unique=True
    )
    academy = models.ForeignKey(
        "SharedAcademy",
        help_text=_('The academy this user belongs to.'),
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_academy_related",
        on_delete=models.CASCADE
    )

    # DEVELOPERS NOTE:
    # WE WILL BE USING "EMAIL" AND "ACADEMY" AS THE UNIQUE PAIR THAT WILL
    # DETERMINE WHETHER THE AN ACCOUNT EXISTS. WE ARE DOING THIS TO SUPPORT
    # TENANT SPECIFIC USER ACCOUNTS WHICH DO NOT EXIST ON OTHER TENANTS.
    # WE USE CUSTOM "AUTHENTICATION BACKEND" TO SUPPORT THE LOGGING IN.
    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = []

    objects = SharedUserManager()

    class Meta:
        app_label = 'shared_foundation'
        db_table = 'at_users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        unique_together = ('email', 'academy',)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this SharedUser.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def generate_pr_code(self):
        """
        Function generates a new password reset code and expiry date.
        """
        self.pr_access_code = get_random_string(length=127)
        self.pr_expiry_date = get_expiry_date()
        self.save()
        return self.pr_access_code

    def has_pr_code_expired(self):
        """
        Returns true or false depending on whether the password reset code
        has expired or not.
        """
        today = timezone.now()
        return today >= self.pr_expiry_date
