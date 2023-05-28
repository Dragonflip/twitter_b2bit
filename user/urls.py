from django.urls import path
from user import api

urlpatterns = [
    path('register/', api.RegisterApi.as_view(), name='register'),
    path('token/', api.TokenApi.as_view(), name='token'),
    path('profile', api.ProfileApi.as_view(), name='profile')
]
