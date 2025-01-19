from django.urls import path
from .views import NetworkGenerator


urlpatterns = [
    path('network-generator/', NetworkGenerator.as_view(), name='network_generator'),
]