import pytest
from django.contrib.auth.models import User
from posts.models import Post
from user.services import create_token


@pytest.fixture
def new_user():
    user = User(
        username="test_user",
        first_name="test_user",
        last_name="test_user",
        email="test_user",
    )
    user.set_password('test_user')
    user.save()
    return user

@pytest.fixture
def new_users():
    users = []
    for i in range(5):
        user = User(
            username=f"test_user{i}",
            first_name="test_user",
            last_name="test_user",
            email="test_user{i}@email.com",
        )
        user.set_password('test_user')
        user.save()
        users.append(user)
    return users

@pytest.fixture
def token_user(new_user):
    return create_token(new_user)

@pytest.fixture
def new_posts(new_users):
    posts = []
    for user in new_users:
        post = Post.objects.create(
            owner=user,
            text=f'post from {user.username}'
        ) 
        posts.append(post)

    return posts
