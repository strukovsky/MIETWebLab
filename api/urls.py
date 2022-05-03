from django.urls import path
from .views import AuthView, CommentsView

urlpatterns = [
    path("authenticate/", AuthView.as_view()),
    path("authenticate", AuthView.as_view()),
    path("comments", CommentsView.as_view()),
    path("comments/", CommentsView.as_view()),
]
