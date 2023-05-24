from django.contrib.auth.models import User
from rest_framework import response, views, status
from user import serializers as user_serializer
from user import services as user_services


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


"""
class LoginApi(views.APIView):

    def post(self, request):
        serializer = user_serializer.LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            if user_services.authenticate(username, password):
                token = user_services.create_token(username)
                resp = response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    user = User.objects.filter(username=username).first()
                resp.set_cookie(key='jwt', value=token)
                return resp

        resp = response.Response(status=status.HTTP_401_UNAUTHORIZED)
        return resp
"""
