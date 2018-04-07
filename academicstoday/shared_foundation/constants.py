# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# The domain of our application.
#

AT_APP_HTTP_PROTOCOL = settings.AT_APP_HTTP_PROTOCOL
AT_APP_HTTP_DOMAIN = settings.AT_APP_HTTP_DOMAIN


# The groups of our application.
#

EXECUTIVE_GROUP_ID = 1
MANAGEMENT_GROUP_ID = 2
FRONTLINE_GROUP_ID = 3
ASSOCIATE_GROUP_ID = 4
CUSTOMER_GROUP_ID = 5


# The default currency of our application.
#

AT_APP_DEFAULT_MONEY_CURRENCY = settings.AT_APP_DEFAULT_MONEY_CURRENCY
