from django.urls import reverse
from rest_framework import status
import pytest

def test_post_unauthorized_fail(client):
    url = reverse('posts')
    data = {'text': 'test_post'} 

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_unauthorized_fail(client):
    url = reverse('posts')

    response = client.get(url)

    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_post_authorized_succeeded(client, token_user):
    url = reverse('posts')
    data = {'text': 'test_post'} 
    headers = {'Authorization': f'Bearer {token_user}'}

    response = client.post(url, data, headers=headers, format='json')

    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_get_unauthorized_succeeded(client, token_user):
    url = reverse('posts')
    headers = {'Authorization': f'Bearer {token_user}'}

    response = client.get(url, headers=headers)

    assert response.status_code == status.HTTP_200_OK

