from django.urls import path
from .views import index, grammar, vocabulary, authenticate

urlpatterns = [
    path('', index, name="index"),
    path('grammar', grammar, name="grammar"),
    path('vocabulary', vocabulary, name="vocabulary"),
    path('authenticate', authenticate, name="authenticate"),
]