from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentCreateView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<pk>', PostRetrieveUpdateDestroyView.as_view()),
    path('<pk>/comments', CommentCreateView.as_view()),
]
