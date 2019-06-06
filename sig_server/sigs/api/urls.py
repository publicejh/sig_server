from django.urls import path
from .views import SigListCreateView, SigRetrieveUpdateDestroyView, SigParticipateCreateView, SigParticipateListView

urlpatterns = [
    path('', SigListCreateView.as_view()),
    path('<pk>/', SigRetrieveUpdateDestroyView.as_view()),
    path('<pk>/invite/', SigParticipateCreateView.as_view()),
    path('<int:sig_id>/members/', SigParticipateListView.as_view()),
]
