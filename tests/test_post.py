from posts.models import Post
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_post_authorized_succeeded(client, token_user):
    url = reverse('posts')
    data = {'text': 'test_post'} 
    headers = {'Authorization': f'Bearer {token_user}'}

    client.post(url, data, headers=headers, format='json')
    post = Post.objects.first()
    assert post.text == data.get('text')

@pytest.mark.django_db
def test_owner_cant_see_their_posts(client, token_user, new_posts):
    url = reverse('posts')
    data = {'text': 'test_post'} 
    headers = {'Authorization': f'Bearer {token_user}'}

    client.post(url, data, headers=headers, format='json')

    response = client.get(url, headers=headers)

    assert len(response.data) == len(new_posts)
