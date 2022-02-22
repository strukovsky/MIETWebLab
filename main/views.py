from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'Index.html')


def vocabulary(request: HttpRequest) -> HttpResponse:
    return render(request, 'Vocabulary.html')


def grammar(request: HttpRequest) -> HttpResponse:
    return render(request, 'Grammar.html')


def authenticate(request: HttpRequest) -> HttpResponse:
    return render(request, 'Authenticate.html')
