from django.urls import path
from .views import SigList, SigRetrieveUpdateDestroyView

urlpatterns = [
    path('', SigList.as_view()),
    path('<pk>/', SigRetrieveUpdateDestroyView.as_view()),
]
