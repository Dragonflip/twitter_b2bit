from .models import Post
from rest_framework import response, status, views
from .serializers import PostSerializer
from rest_framework import permissions


class PostApi(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.exclude(owner=request.user.id).all()
        print(posts)
        serializer = PostSerializer(posts, many=True)
        print(serializer)
        return response.Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        print(request.user)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
