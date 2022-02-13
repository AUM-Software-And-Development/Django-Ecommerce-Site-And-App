import pytest
from django.core.management import call_command


@pytest.fixture
def create_admin_user(django_user_model):
    '''
    Return admin user
    '''
    return django_user_model.objects.create_superuser('superuser', '', 'xyz')

@pytest.fixture(scope='session')
def db_fixture_setup(django_db_setup, django_db_blocker):
    '''
    Unlocks database and uses fixtures as inserts
    '''
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
