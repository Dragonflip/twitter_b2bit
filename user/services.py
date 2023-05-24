import datetime
import jwt
from django.conf import settings
from django.contrib.auth.models import User


def authenticate(username, password):
    user = User.objects.filter(username=username).first()
    if user:
        return user.check_password(password)

    return False

def create_token(username):
    user = User.objects.filter(username=username).first()
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
    return token
