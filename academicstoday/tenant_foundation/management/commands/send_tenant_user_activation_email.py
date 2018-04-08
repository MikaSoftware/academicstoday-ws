# -*- coding: utf-8 -*-
import django_rq
from starterkit.utils import (
    get_random_string,
    get_unique_username_from_email
)
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMultiAlternatives    # EMAILER
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string    # HTML to TXT
from shared_foundation import constants
from shared_foundation.models import SharedUser
from shared_foundation.utils import reverse_with_full_domain


class Command(BaseCommand):
    help = _('Command will send an activation email to the user based on the username or email.')

    def add_arguments(self, parser):
        # User Account.
        parser.add_argument('email' , nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            for email in options['email']:
                me = SharedUser.objects.get(email__iexact=email)

                if me.academy is None:
                    raise CommandError(_('Account does not belong to a tenant!'))

                if me.academy.activation_callback_url is None:
                    raise CommandError(_('Academy does not contain an activation callback url.'))

                self.begin_processing(me)
        except SharedUser.DoesNotExist:
            raise CommandError(_('Account does not exist with the email: %s') % str(email))

        # Return success message.
        self.stdout.write(
            self.style.SUCCESS(_('AT tenant activation email was sent successfully.'))
        )

    def begin_processing(self, me):
        # We will generate the URL which will take the user to the client's website.
        pr_access_code = me.generate_pr_code()
        client_side_url = me.academy.activation_callback_url.replace("{{ pr_access_code }}", pr_access_code)

        #TODO: Added "web_view_url" in future.

        subject = "Welcome!"
        param = {
            'me': me,
            'url': client_side_url,
            'constants': constants
        }

        # Plug-in the data into our templates and render the data.
        text_content = render_to_string('tenant_foundation/email/user_activation_email_view.txt', param)
        html_content = render_to_string('tenant_foundation/email/user_activation_email_view.html', param)

        # Generate our address.
        from_email = settings.DEFAULT_FROM_EMAIL
        to = [me.email]

        # Send the email.
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
