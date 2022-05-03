from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from api.models import Comment


def index(request: HttpRequest) -> HttpResponse:
    comment_form = CommentForm()
    return render(request, 'Index.html', {"comment_form": comment_form})


def vocabulary(request: HttpRequest) -> HttpResponse:
    return render(request, 'Vocabulary.html')


def grammar(request: HttpRequest) -> HttpResponse:
    return render(request, 'Grammar.html')


def authenticate(request: HttpRequest) -> HttpResponse:
    return render(request, 'Authenticate.html')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
