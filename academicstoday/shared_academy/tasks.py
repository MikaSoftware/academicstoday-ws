from rq import get_current_job
from django_rq import job
from django.core.management import call_command


@job
def create_academy_func(data_dict):
    # print(data_dict) # For debugging purposes only.
    call_command(
        'create_academy',
        data_dict['user_pk'],
        data_dict['schema_name'],
        data_dict['name'],
        data_dict['alternate_name']
    )
