import pytest
from django.contrib.auth.models import User 

# create a Pytest mark to test user creation so as to access the db 
@pytest.mark.django_db
def create_user_test():
    User.objects.create_user('momoapi', 'momoapi@mwanjajoel.com', 'momopassword')
    assert User.objects.count() == 1