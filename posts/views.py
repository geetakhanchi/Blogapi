from django.contrib.auth import get_user_model 
from rest_framework import viewsets #new
from .models import Post
from .permissios import IsAuthorOrReadOnly 
from .serializers import PostSerializer, UserSerializer


class PostViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)  
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class UserViewsets(viewsets.ModelViewSet): #new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
       