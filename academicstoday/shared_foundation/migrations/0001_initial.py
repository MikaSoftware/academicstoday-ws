# Generated by Django 2.0.4 on 2018-04-07 23:25

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django_tenants.postgresql_backend.base
import phonenumber_field.modelfields
import shared_foundation.models.user
import starterkit.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, db_index=True, help_text='The users given name.', max_length=63, null=True, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, db_index=True, help_text='The users middle name.', max_length=63, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(blank=True, db_index=True, help_text='The users last name.', max_length=63, null=True, verbose_name='Last Name')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('birthdate', models.DateField(blank=True, help_text='The users birthdate.', null=True, verbose_name='Birthdate')),
                ('join_date', models.DateTimeField(blank=True, help_text='The date the customer joined this organization.', null=True, verbose_name='Join Date')),
                ('nationality', models.CharField(blank=True, help_text='Nationality of the person.', max_length=63, null=True, verbose_name='Nationality')),
                ('gender', models.CharField(blank=True, help_text='Gender of the person. While Male and Female may be used, text strings are also acceptable for people who do not identify as a binary gender.', max_length=63, null=True, verbose_name='Gender')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('was_email_activated', models.BooleanField(default=False, help_text='Was the email address verified as an existing address?', verbose_name='Was Email Activated')),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('salt', models.CharField(blank=True, default=starterkit.utils.generate_hash, help_text='The unique salt value me with this object.', max_length=127, null=True, unique=True, verbose_name='Salt')),
                ('type_of', models.PositiveSmallIntegerField(blank=True, db_index=True, default=0, help_text='The type of user this is. Value represents ID of user type.', verbose_name='Type of')),
                ('is_ok_to_email', models.BooleanField(default=True, help_text='Indicates whether customer allows being reached by email', verbose_name='Is OK to email')),
                ('is_ok_to_text', models.BooleanField(default=True, help_text='Indicates whether customer allows being reached by text.', verbose_name='Is OK to text')),
                ('pr_access_code', models.CharField(blank=True, default=starterkit.utils.generate_hash, help_text='The access code to enter the password reset page to be granted access to restart your password.', max_length=127, verbose_name='Password Reset Access Code')),
                ('pr_expiry_date', models.DateTimeField(blank=True, default=shared_foundation.models.user.get_expiry_date, help_text='The date where the access code expires and no longer works.', verbose_name='Password Reset Access Code Expiry Date')),
                ('area_served', models.CharField(blank=True, help_text='The geographic area where a service or offered item is provided.', max_length=127, null=True, verbose_name='Area Served')),
                ('available_language', models.CharField(blank=True, help_text='A language someone may use with or at the item, service or place. Please use one of the language codes from the <a href="https://tools.ietf.org/html/bcp47">IETF BCP 47 standard</a>.', max_length=127, null=True, verbose_name='Available Language')),
                ('contact_type', models.CharField(blank=True, help_text='A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.', max_length=127, null=True, verbose_name='Contact Type')),
                ('email', models.EmailField(db_index=True, help_text='Email address.', max_length=254, verbose_name='Email')),
                ('fax_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='The fax number.', max_length=128, null=True, verbose_name='Fax Number')),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, help_text='The telephone number.', max_length=128, null=True, verbose_name='Telephone')),
                ('telephone_extension', models.CharField(blank=True, help_text='The telephone number.', max_length=31, null=True, verbose_name='Telephone Extension')),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, help_text='The mobile telephone number.', max_length=128, null=True, verbose_name='Mobile')),
                ('elevation', models.FloatField(blank=True, help_text='The elevation of a location (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).', null=True, verbose_name='Elevation')),
                ('latitude', models.DecimalField(blank=True, decimal_places=3, help_text='The latitude of a location. For example 37.42242 (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).', max_digits=8, null=True, verbose_name='Latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=3, help_text='The longitude of a location. For example -122.08585 (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).', max_digits=8, null=True, verbose_name='Longitude')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, db_index=True, help_text='A longitude and latitude coordinates of this location.', null=True, srid=4326, verbose_name='Location')),
                ('address_country', models.CharField(blank=True, help_text='The country. For example, USA. You can also provide the two-letter <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1 alpha-2</a> country code.', max_length=127, null=True, verbose_name='Address Country')),
                ('address_locality', models.CharField(blank=True, help_text='The locality. For example, Mountain View.', max_length=127, null=True, verbose_name='Address Locaility')),
                ('address_region', models.CharField(blank=True, help_text='The region. For example, CA.', max_length=127, null=True, verbose_name='Address Region')),
                ('post_office_box_number', models.CharField(blank=True, help_text='Apartment, suite, unit, building, floor, etc.', max_length=255, null=True, verbose_name='Post Office Box Number')),
                ('postal_code', models.CharField(blank=True, db_index=True, help_text='The postal code. For example, 94043.', max_length=127, null=True, verbose_name='Postal Code')),
                ('street_address', models.CharField(blank=True, help_text='The street address. For example, 1600 Amphitheatre Pkwy.', max_length=255, null=True, verbose_name='Street Address')),
                ('street_address_extra', models.CharField(blank=True, help_text='Apartment, suite, unit, building, floor, etc.', max_length=255, null=True, verbose_name='Street Address (Extra Line)')),
                ('identifier', models.CharField(db_index=True, help_text='The unique identifier which has email plus a tenant_id number appended to it. If no tenant_id is append then this user has not been assigned anywhere.', max_length=255, unique=True, verbose_name='Identifier')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'at_users',
            },
            managers=[
                ('objects', shared_foundation.models.user.SharedUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SharedAcademy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('alternate_name', models.CharField(blank=True, help_text='An alias for the item.', max_length=255, null=True, verbose_name='Alternate Name')),
                ('description', models.TextField(blank=True, default='', help_text='A short description of the item.', null=True, verbose_name='Description')),
                ('name', models.CharField(blank=True, default='', help_text='The name of the item.', max_length=255, null=True, verbose_name='Name')),
                ('url', models.URLField(blank=True, help_text='URL of the item.', null=True, verbose_name='URL')),
                ('area_served', models.CharField(blank=True, help_text='The geographic area where a service or offered item is provided.', max_length=127, null=True, verbose_name='Area Served')),
                ('available_language', models.CharField(blank=True, help_text='A language someone may use with or at the item, service or place. Please use one of the language codes from the <a href="https://tools.ietf.org/html/bcp47">IETF BCP 47 standard</a>.', max_length=127, null=True, verbose_name='Available Language')),
                ('contact_type', models.CharField(blank=True, help_text='A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.', max_length=127, null=True, verbose_name='Contact Type')),
                ('email', models.EmailField(blank=True, help_text='Email address.', max_length=254, null=True, verbose_name='Email')),
                ('fax_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='The fax number.', max_length=128, null=True, verbose_name='Fax Number')),
                ('product_supported', models.CharField(blank=True, default='', help_text='The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").', max_length=31, null=True, verbose_name='Product Supported')),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='The telephone number.', max_length=128, null=True, verbose_name='Telephone')),
                ('telephone_extension', models.CharField(blank=True, default='', help_text='The telephone number.', max_length=31, null=True, verbose_name='Telephone Extension')),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, help_text='The mobile telephone number.', max_length=128, null=True, verbose_name='Mobile')),
                ('address_country', models.CharField(help_text='The country. For example, USA. You can also provide the two-letter <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1 alpha-2</a> country code.', max_length=127, verbose_name='Address Country')),
                ('address_locality', models.CharField(help_text='The locality. For example, Mountain View.', max_length=127, verbose_name='Address Locaility')),
                ('address_region', models.CharField(help_text='The region. For example, CA.', max_length=127, verbose_name='Address Region')),
                ('post_office_box_number', models.CharField(blank=True, help_text='Apartment, suite, unit, building, floor, etc.', max_length=255, null=True, verbose_name='Post Office Box Number')),
                ('postal_code', models.CharField(blank=True, db_index=True, help_text='The postal code. For example, 94043.', max_length=127, null=True, verbose_name='Postal Code')),
                ('street_address', models.CharField(help_text='The street address. For example, 1600 Amphitheatre Pkwy.', max_length=255, verbose_name='Street Address')),
                ('street_address_extra', models.CharField(blank=True, help_text='Apartment, suite, unit, building, floor, etc.', max_length=255, null=True, verbose_name='Street Address (Extra Line)')),
                ('elevation', models.FloatField(blank=True, help_text='The elevation of a location (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).', null=True, verbose_name='Elevation')),
                ('latitude', models.DecimalField(blank=True, decimal_places=3, help_text='The latitude of a location. For example 37.42242 (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).', max_digits=8, null=True, verbose_name='Latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=3, help_text='The longitude of a location. For example -122.08585 (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).', max_digits=8, null=True, verbose_name='Longitude')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, db_index=True, help_text='A longitude and latitude coordinates of this location.', null=True, srid=4326, verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Franchise',
                'verbose_name_plural': 'Franchises',
                'db_table': 'at_academies',
                'permissions': (('can_get_academys', 'Can get academys'), ('can_get_academy', 'Can get academy'), ('can_post_academy', 'Can post academy'), ('can_put_academy', 'Can put academy'), ('can_delete_academy', 'Can delete academy')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SharedAcademyDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='shared_foundation.SharedAcademy')),
            ],
            options={
                'verbose_name': 'Domain',
                'verbose_name_plural': 'Domains',
                'db_table': 'atacademy_domains',
            },
        ),
        migrations.CreateModel(
            name='SharedOpeningHoursSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('alternate_name', models.CharField(blank=True, help_text='An alias for the item.', max_length=255, null=True, verbose_name='Alternate Name')),
                ('description', models.TextField(blank=True, default='', help_text='A short description of the item.', null=True, verbose_name='Description')),
                ('name', models.CharField(blank=True, default='', help_text='The name of the item.', max_length=255, null=True, verbose_name='Name')),
                ('url', models.URLField(blank=True, help_text='URL of the item.', null=True, verbose_name='URL')),
                ('closes', models.CharField(blank=True, help_text='The closing hour of the place or service on the given day(s) of the week.', max_length=15, null=True, verbose_name='Closes')),
                ('day_of_week', models.CharField(blank=True, help_text='The day of the week for which these opening hours are valid.', max_length=15, null=True, verbose_name='Day Of Week')),
                ('opens', models.CharField(blank=True, help_text='The opening hour of the place or service on the given day(s) of the week.', max_length=15, null=True, verbose_name='Opens')),
                ('valid_from', models.DateField(blank=True, help_text='The date when the item becomes valid.', null=True, verbose_name='Valid From')),
                ('valid_through', models.DateField(blank=True, help_text='The end of the validity of offer, price specification, or opening hours data.', null=True, verbose_name='Valid Through')),
                ('owner', models.ForeignKey(blank=True, help_text='The user whom owns this thing.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_foundation_sharedopeninghoursspecification_abstract_thing_owner_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Opening Hours Specification',
                'verbose_name_plural': 'Opening Hours Specifications',
                'db_table': 'at_opening_hours_specifications',
                'permissions': (('can_get_opening_hours_specifications', 'Can get opening hours specifications'), ('can_get_opening_hours_specification', 'Can get opening hours specifications'), ('can_post_opening_hours_specification', 'Can create opening hours specifications'), ('can_put_opening_hours_specification', 'Can update opening hours specifications'), ('can_delete_opening_hours_specification', 'Can delete opening hours specifications')),
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='sharedacademy',
            name='hours_available',
            field=models.ManyToManyField(blank=True, help_text='The hours during which this service or contact is available.', related_name='shared_foundation_sharedacademy_contact_point_hours_available_related', to='shared_foundation.SharedOpeningHoursSpecification'),
        ),
        migrations.AddField(
            model_name='sharedacademy',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='The user whom owns this thing.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_foundation_sharedacademy_abstract_thing_owner_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shareduser',
            name='academy',
            field=models.ForeignKey(blank=True, help_text='The academy this user belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_foundation_shareduser_academy_related', to='shared_foundation.SharedAcademy'),
        ),
        migrations.AddField(
            model_name='shareduser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='shareduser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='shareduser',
            unique_together={('email', 'academy')},
        ),
    ]
