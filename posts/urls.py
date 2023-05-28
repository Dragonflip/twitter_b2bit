from django.urls import path
from . import api

urlpatterns = [
    path("", api.PostApi.as_view(), name="posts"),
    #    path('detail_post/<int:pk>/', api.LoginApi.as_view(), name='detail_post'),
]
