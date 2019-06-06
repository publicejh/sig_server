from rest_framework import generics
from rest_framework.response import Response
from posts.models import Post, Comment
from .serializers import PostDetailSerializer, CommentDetailSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def get_queryset(self):
        sig_id = self.request.query_params.get('sigId', None)
        queryset = Post.objects.filter(sig_id=sig_id)
        return queryset.order_by('-id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostDetailSerializer(queryset, many=True)
        return Response(serializer.data)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment
    serializer_class = CommentDetailSerializer
