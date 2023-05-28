from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import response, views, status
from user import serializers as user_serializer
from user import services as user_services
from rest_framework import permissions


class RegisterApi(views.APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = user_serializer.UserSerializer(users, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApi(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if user:
            serializer = user_serializer.ProfileSerializer(user.profile)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            user = authenticate(username=username, password=password)
            if user:
                token = user_services.create_token(user)
                resp = response.Response(
                    serializer.data, status=status.HTTP_202_ACCEPTED
                )
                resp.set_cookie(key="jwt", value=token)
                return resp

        resp = response.Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        return resp
