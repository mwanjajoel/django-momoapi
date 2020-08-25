import pytest
from django.contrib.auth.models import User 

# create a Pytest mark to test user creation so as to access the db 
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user(
        username='momoapi', 
        email='momoapi@mwanjajoel.com', 
        password='momopassword')
    assert User.objects.count() == 1