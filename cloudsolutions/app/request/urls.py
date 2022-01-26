from django.urls import path
from app.request.views import index_request

urlpatterns = [
    path('', index_request),
]
