from django.urls import path
from app.service.views import index

urlpatterns = [
    path('', index),
]
