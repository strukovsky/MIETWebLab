from django.urls import path
from .views import AuthView

urlpatterns = [
    path("authenticate/", AuthView.as_view()),
    path("authenticate", AuthView.as_view()),
]
