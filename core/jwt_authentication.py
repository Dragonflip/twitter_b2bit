import jwt
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework import authentication, exceptions


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = self.get_token_from_request(request)

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("Invalid Token")
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Expired Token")

        id = payload.get("id")
        user = User.objects.filter(id=id).first()
        return (user, token)

    def get_token_from_request(self, request):
        authorization_header = request.headers.get("Authorization")

        if authorization_header:
            try:
                scheme, token = authorization_header.split()
                if scheme.lower() != "bearer":
                    raise exceptions.AuthenticationFailed(
                        "Authentication scheme invalid"
                    )
                return token
            except ValueError:
                raise exceptions.AuthenticationFailed("Invalid Token")
        return None
