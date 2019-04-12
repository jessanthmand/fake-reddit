from .models import Comments, Posts
from rest_framework import viewsets
from .serializers import CommentsSerializer, PostsSerializer

# Create your views here.
class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class PostsView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer




