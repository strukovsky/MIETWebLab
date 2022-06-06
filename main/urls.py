from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.models import User

from app import settings
from .views import index, grammar, vocabulary, authenticate

urlpatterns = [
    path('', index, name="index"),
    path('grammar', grammar, name="grammar"),
    path('vocabulary', vocabulary, name="vocabulary"),
    path('authenticate', authenticate, name="authenticate"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
