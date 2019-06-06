from django.urls import path
from .views import SigListCreateView, SigRetrieveUpdateDestroyView, SigParticipateCreateView,\
    SigParticipateListCreateView, SigInvitationTokenCreateView, SigInvitationTokenRetrieveView

urlpatterns = [
    path('', SigListCreateView.as_view()),
    path('<pk>/', SigRetrieveUpdateDestroyView.as_view()),
    path('<pk>/invite/', SigParticipateCreateView.as_view()),
    path('<int:sig_id>/members/', SigParticipateListCreateView.as_view()),
    path('<int:sig_id>/invitations/', SigInvitationTokenCreateView.as_view()),
    path('n/<token>', SigInvitationTokenRetrieveView.as_view()),
]
