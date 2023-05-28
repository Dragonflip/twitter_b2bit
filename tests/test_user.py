from django.contrib.auth.models import User
import jwt
from django.conf import settings
from user.models import Profile
from django.urls import reverse
from rest_framework import status
import pytest


@pytest.mark.django_db
def test_profile_created_with_user(new_user):
    profile = Profile.objects.filter(user=new_user).all()
    assert len(profile) == 1

@pytest.mark.django_db
def test_create_user(client):
    url = reverse('register')
    data = {
        'username': 'test_user',
        'password': 'test_password',
        'email': 'test@email.com'
    }

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_create_user_with_same_name_should_fail(client, new_user):
    url = reverse('register')
    data = {
        'username': new_user.username,
        'password': 'test_password',
        'email': new_user.email
    }

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_get_users(client, new_users):
    url = reverse('register')

    response = client.get(url)

    assert len(response.data) == len(new_users)

@pytest.mark.django_db
def test_token_user(client, new_user):
    url = reverse('token')
    data = {
        'username': new_user.username,
        'password': 'test_user'
    }

    response = client.post(url, data, format='json')
    
    token_cookie = response.cookies.get('jwt')
    token = token_cookie.value

    payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
    id = payload.get('id')
    assert id == new_user.id
