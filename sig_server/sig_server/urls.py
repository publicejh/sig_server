from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sig-management/doc/', get_swagger_view(title='Rest API Document')),
    path('sig-management/v1/sigs/', include('sigs.api.urls')),
]
